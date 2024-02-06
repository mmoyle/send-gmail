import argparse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import yaml
from jinja2 import Environment, FileSystemLoader

def read_yaml_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def render_template(template_path, variables):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    return template.render(variables)

def send_email(subject, body, to_email, smtp_config):
    msg = MIMEMultipart()
    msg['From'] = smtp_config['from_email']
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    with smtplib.SMTP_SSL(smtp_config['smtp_server'], smtp_config['smtp_port']) as server:
        #server.starttls()
        server.login(smtp_config['from_email'], smtp_config['app_password'])
        server.sendmail(smtp_config['from_email'], to_email, msg.as_string())

def main():
    parser = argparse.ArgumentParser(description='Send emails based on the email type.')
    parser.add_argument('--template', choices=['new-workspace', 'reset-password'],
                        help='Type of email to send: new_workspace or password_reset')
    parser.add_argument('--recipients',help='Yaml file of recipients')

    args = parser.parse_args()
    config = read_yaml_config('config.yaml')  # Replace with your YAML config file path
    config['smtp']['app_password'] = read_yaml_config('config-secret.yaml')['app_password']

    smtp_config = config['smtp']

    template_path = f'templates/{args.template}.jinja'

    recipients = read_yaml_config(args.recipients)
    subject = config['template'][args.template]['subject']

    for recipient in recipients:
        body = render_template(template_path, recipient)
        to_email = recipient['email']
        send_email(subject, body, to_email, smtp_config)

if __name__ == "__main__":
    main()

# README #

## Setup ##

### Install pip3 packages (Mac OS)



```
pip3 install jinja2 PyYAML

```

### Create an app password for gmail
This will be under MFA in the googl settings.


### Create config-secret.yaml
This will contain your app password so is ignored by git

```
app_password: aaaa bbbb aaaa bbbb
```

### Create recipients.yaml
```
- first_name: Zara
  user_name: zara.neo
  email: zara.neo@cybernetix.eu
- first_name: Cipher
  user_name: cipher.shadow
  email: cipher.shadow@cybernetix.eu
  secret_link: https://onetimesecret.com/secret/fffffffxxxxxxxbbbbbbbbb
```

# Running

```
$ python3 send-email.py --template reset-password --recipients test-recipients.yaml
```

Help message

```
$ python3 send-email.py -h
```


## See
https://mailtrap.io/blog/python-send-email-gmail/
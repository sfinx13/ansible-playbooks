# Ansible - Deploy symfony demo on Ubuntu 20.04

This playbook will install symfony demo on an ubuntu 20.04 machine. It has been tested with docker container.

## Prerequisites
Make sure you have installed all of the following prerequisites on your development machine:
* Docker - [Download & Install Docker](https://docs.docker.com/engine/install/). 

## Playbook
```
symfony-lemp_ubuntu20.04/
├── .config/
├── playbooks/
│   ├── roles/
│   └── main.yml
├── vars/
│   └── default.yml
├── ansible.cfg
├── build.sh
├── run.sh
├── Dockerfile
└── inventory
```

## Settings  `vars/default.yml`

- `http_host`: your domain name
- `www_path`: your web app root folder 
- `git_url_repository`: your git url repository to clone
- `git_branch`: your branch name
- `mysql_root_password`: your root password
- `mysql_database_url`: your credentiels database
- `db_user`: your database user
- `db_password`: your database password
- `db_host`: your database host
- `db_port`: your database port
- `db_name`: your database name
- `app_secret`: your symfony secret
- `app_env`: define dev ou prod environment
- `symfony_console_path`: your symfony console absolute path

## Secrets `vars/secrets.yml`

To display the contents of an encrypted ansible-vault file without modifying it, just use the view option

```bash
$ ansible-vault view vars/secrets.yml
```
Vault password is `secret`

## Runnning the playbook
Quick steps after cloning the repository

### 0. Edit /etc/hosts
```
127.0.0.1       node-1
127.0.0.1       node-2
```

### 1. Get the playbook

```bash
$ cd ansible-playbooks/symfony-lemp_ubuntu20.04
```

### 2. Customize options
```bash
$ vi vars/default.yml
```

### 3. Instll pip dependencies
```bash
$ pip install -r requirements.txt
```

### 4. Enable the logs on node manager
```bash
$ touch /var/log/ansible.log 
$ chmod 640 /var/log/ansible.log
$ chown [OWNER]:[GROUP] /var/log/ansible.log
```

### 5. Launch docker container to test the playbook
```bash
./build.sh
./run.sh # Expose port 80 from container and map with host port 8080
```
Check if node target is pingable
```
ansible all -m ping
```

```
node-1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
node-2 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

### 6. Run the playbook
> Add ask-pass option is useful the first time, cause need to copy public key to the server
```command
ansible-playbook -v -i inventory --ask-pass --ask-vault-pass playbooks/main.yml
```

### 6.1 Run ad-hoc command if nginx and php8.1-fpm service failed to restart
```bash
ansible all -m raw -a 'service php8.1-fpm restart'
```  

```
node-1 | CHANGED | rc=0 >>
 * Restarting PHP 8.1 FastCGI Process Manager php-fpm8.1                 [ OK ] 
Connection to node-1 closed.

node-2 | CHANGED | rc=0 >>
 * Restarting PHP 8.1 FastCGI Process Manager php-fpm8.1                 [ OK ] 
Connection to node-2 closed.
```

```bash
ansible all -m raw -a 'service nginx restart'
```

```
node-1 | CHANGED | rc=0 >>
 * Restarting nginx nginx                                                [ OK ] 
Connection to node-1 closed.

node-2 | CHANGED | rc=0 >>
 * Restarting nginx nginx                                                [ OK ] 
Connection to node-2 closed.
```

### 7. Welcome page It works

| node-1                     | node-2                    |
-----------------------------|---------------------------|
|💻 http://node-1:8080/fr | 💻 http://node-2:8081/fr|

![screenshot](images/homepage_symfony_demo.jpg)

#### 8. Run check-http task in the playbook

```
$ cd symfony-lemp_ubuntu20.04
$ ansible-playbook --ask-vault-password playbooks/http_status.yml 
```

```
PLAY [Deploy Symfony Demo Application] ************************************************************************************

TASK [check-http : check that homepage returns a status 200] **************************************************************
ok: [node-2] => (item=8080)
ok: [node-1] => (item=8080)
ok: [node-2] => (item=8081)
ok: [node-1] => (item=8081)came

PLAY RECAP ****************************************************************************************************************
node-1                     : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
node-2                     : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

#### 8. Run custom playbook written in python

```command
$ cd symfony-lemp_ubuntu20.04
$ ansible-playbook --syntax-check -i inventory playbooks/count_post.yml --ask-vault-pass
```

## Documentation

[Encrypting content with Ansible Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html)

[Developing Ansible modules](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html)

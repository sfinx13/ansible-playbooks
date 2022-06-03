# Symfony Demo on Ubuntu 20.04

This playbook will install Symfony demo on an Ubuntu 20.04 machine

## Settings
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

## Your playbook
👉🏿 ![_IMG/tree_playbook.jpg](_IMG/tree_playbook.jpg)

## Runnning this Playbook
Quick steps after cloning the repository

### 1. Get the playbook

```bash
cd ansible-playbooks/symfony-lemp_ubuntu20.04
```

### 2. Customize options
```bash
vi vars/default.yml
```

### 3. Enable the logs on node manager
```bash
touch /var/log/ansible.log 
chmod 640 /var/log/ansible.log
chown [OWNER]:[GROUP] /var/log/ansible.log
```

### 4. Launch docker container to test the playbook
```bash
./build.sh
./run.sh # Expose port 80 from container and map with host port 8080
```

### 5. Run the Playbook
> ask-pass option is useful the first time, cause need to copy public key to the server
```command
ansible-playbook -v -i inventory playbooks/main.yml --ask-pass
```

### 6. Welcome page It works
✌️ http://localhost:8080/fr

👉🏿 ![__IMG/homepage_symfony_demo.jpg](__IMG/homepage_symfony_demo.jpg)
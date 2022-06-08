#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule
import MySQLdb


def main():
    module = AnsibleModule(
        argument_spec=dict(
            db_user=dict(require=True, type='str'),
            db_password=dict(require=True, type='str'),
            db_name=dict(require=True, type='str'),
            request=dict(require=True, type='str'),
        )
    )

    db_user_param = module.params.get('db_user')
    db_password_param = module.params.get('db_password')
    db_name_param = module.params.get('db_name')
    request_param = module.params.get('request')

    database = MySQLdb.connect(
        user=db_user_param,
        password=db_password_param,
        db=db_name_param)

    cursor = database.cursor()
    cursor.execute(request_param)
    results = cursor.fetchall()
    database.close()

    module.exit_json(changed=False, results=results)


if __name__ == "__main__":
    main()


DOCUMENTATION = r'''
module: count_post
author: Saidi
description: Module that allows you to execute an SQL query
options:
  db_user:
    description: Database user
    required: yes
  db_password:
    description: Database password
    required: yes
  db_name:
    description: Database name
    required: yes
  request:
    description: SQL query to execute
    required: yes
'''

EXAMPLES = r'''
- name: "Count the number of posts"
    count_post:
        db_user: "{{ db_user }}"
        db_password: "{{ db_password }}"
        db_name: "{{ db_name }}"
        request: "select count(*) from symfony_demo_post"
'''

RETURN = r'''
results:
    description: Request result
'''

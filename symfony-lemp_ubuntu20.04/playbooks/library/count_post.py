#!/usr/bin/python

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

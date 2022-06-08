#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(argument_spec={})
    module.exit_json(changed=False, meta="Hello world")


if __name__ == "__main__":
    main()

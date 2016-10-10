# README.md

# Ansible Role: User v1.0

An Ansible role that creates users, updates passwords, configures authorized_keys file for ssh.

Allows you to specify a different list of users for each host group or within a playbook

It is recommended to ansible-vault encrypt the master_users_list variable

See `files/generate_password_hash.py` to generate compatible password hashes

For each user in master_users_list.users[], `ssh_key` list is lineinfiled into /home/{{ user }}/.ssh/authorized_keys

See Also: ansible-role-sudo, ansible-role-bash

![travis-ci](https://travis-ci.org/mm0/ansible-role-user.svg?branch=master)

## Requirements

Sudo access

## Role Variables

Available variables are listed below, there are no defaults:

    master_users_list: 
      root: # root user handled separately as home directory is different than the rest of users
        password: "$6$..." # password hash
      users:
        username_1:
          groups: username_1, additional_group
          state: present
          password: "$6$rounds=p...." # password hash
          ssh_key:
          - "ssh-rsa ..." #allows for multiple keys
          - "ssh-rsa ... #key 2 for username_1"
        

## Dependencies

None 

## Example Playbook

    - hosts: webservers
      vars:
      - master_users_list:
        users:
          travis:
            groups: travis, additional_group
            state: present
            password: "$6$rounds=100000$76usz5L2Y.bpvtTB$vtivr8XwS0al8MA2q2s/YKEu312l7gHnK3eLkRo9QmKmk5XIIsDDAZmT7Hrc0YaLTQjD7wZ//HbwM49YjsxkJ/" # password hash
            ssh_key:
            - "ssh-rsa 1234"
        
      roles:
      - ansible-role-user

## License

MIT

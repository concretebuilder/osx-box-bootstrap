Role Name
=========

This role is responsible to execute the tests for the roles

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.
You need to have installed molecule and testinfra `pip3 install molecule testinfra`

Flow and Commands
------------

molecule test: will execute the whole flow and test your role

During the development the flow is the following:
 - molecule create: It creates the container that will be user by molecule
 - molecule converge: It will apply the playbook to the previously create container
 - molecule verify: Executes the tests
 - change something in your role
 - molecule converge: apply the changes
 - molecule verify: execute the tests again

So: molecule create -> molecule converge -> molecule verify -> change role -> molecule converge -> molecule verify

Example Playbook
----------------

See brew role

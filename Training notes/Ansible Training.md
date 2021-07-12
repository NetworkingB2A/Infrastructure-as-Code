# Training Ansible

Create a python virtual environment.

<code> python3 -m venv venv </code>

Switch to environment.

<code> source venv/bin/active </code>

install ansible

<code>pip install ansible</code>




## Need to know commands for Ansible
view info about your ansible

<code> ansible --version </code>
<blockquote>
Output

*ansible [core 2.11.2]

    config file = /etc/ansible/ansible.cfg
    configured module search path = ['/home/angella/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
    ansible python module location = /home/angella/Programming/Infrastructure-as-Code/venv/lib/python3.8/site-packages/ansible
    ansible collection location = /home/angella/.ansible/collections:/usr/share/ansible/collections
    executable location = /home/angella/Programming/Infrastructure-as-Code/venv/bin/ansible
    python version = 3.8.10 (default, Jun  2 2021, 10:49:15) [GCC 10.3.0]
    jinja version = 3.0.1
    libyaml = True
  </blockquote>


## Good to know
- If you place an Ansible config file in your directory you are currently in. That will become your new Ansible config. If you don't put the Ansible config file in the directory you are in, the default will be in  /etc/ansible/ansible.cfg

When would you use Jinja Templating vs the cisco IOS module?
- you would use both. the power of a template is that you can update the task in one spot and have logic built into the template that you cant build into the task.
- seems like the best idea would be to use jinja template as you main config.

What is the highest prestidance for Ansible vars
- Host vars
- But what is next
    - Group
    - roles
- If you are doing the same type of task which one will win out
- example
    - snmp 
        - roles-task
        - task in task folder/



first make a template folder
Make a single easy to use template






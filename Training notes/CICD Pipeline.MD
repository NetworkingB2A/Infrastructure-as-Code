What is CICD for network automation?
The goal to to bring software development principles into the net devops mind frame.

How is this done in practice?
network as code
network stored as source control
changes are proposed in code  "branches"
CICD builds test environment, tests code on test environment, then if successful the configuration change will be pushed out to end devices

Tools you will need to preform this ( this is just a list i have come up with, this does not mean you need to follow the tools i have called out)
- Ansible
- CML
- Github(Maybe, might try something else), gogs 
- Drone or Jenkins

steps
- create a branch
- update network to code code
- stage and commit your 
- push your commits to the source control
- Your CICD tool will run the test on the dev branch
- if all tests pass, your CICD tool will push the changes to your production environment



Many steps will be involved for this to happen. (here are some of the steps, need to think about it a bit more before. the steps right now will not be in order)
- need a environment as a "coded network"
- need to have copies of your network 
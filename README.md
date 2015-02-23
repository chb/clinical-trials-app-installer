Clinical Trials App Installer
=============================

Scripts to setup and run a VM hosting the [clinical trials app][app].

1. Install [Vagrant][] and `ansible`
2. Install vagrant plugins:

        vagrant plugin install vagrant-vbguest

3. Install ansible galaxy items:

        ansible-galaxy install Stouts.mongodb

4. Clone this repo:

        git clone --recursive https://github.com/chb/clinical-trials-app-installer
        cd clinical-trials-app-installer

5. Since the app repo is private, we need a deployment key:
    - Create a new SSH key - without setting a password - into a local file named `deploy_key`: `ssh-keygen`
    - Add this key to your repo's "Deployment Keys" on GitHub

6. Adjust `settings.yml` to your liking
7. Get the VM configured:

        vagrant up

8. On your host machine you can now connect to the VM's hosted app at [http://localhost:8080]()

[vagrant]: http://www.vagrantup.com/downloads
[app]: https://github.com/chb/clinical-trials-app

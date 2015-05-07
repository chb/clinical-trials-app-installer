Clinical Trials App Installer
=============================

Scripts to setup and run a VM hosting the [clinical trials app][app].
These scripts take care of provisioning a VM, then installing and setting up Mongo, a lighttpd reverse proxy and all Python modules.
Then the app is installed straight from GitHub.

Perform all the following steps **on your local machine**:

1. Install [Vagrant][] and [Ansible][]
2. Install vagrant plugins:

        vagrant plugin install vagrant-vbguest
        vagrant plugin install vagrant-proxyconf    # only if behind proxy

3. Install ansible galaxy items:

        ansible-galaxy install Stouts.mongodb

4. Clone this repository:

        git clone --recursive https://github.com/chb/clinical-trials-app-installer
        cd clinical-trials-app-installer

5. Since the app repo is private, we need a deployment key:
    - Create a new SSH key - without setting a password - into a local file named `deploy_key`: `ssh-keygen`
    - Add this key to your repo's "Deployment Keys" on GitHub

6. _Optionally_, if you're behind a proxy, add your proxy settings and make sure you installed the _proxyconf_ plugin in step 2:
    - In `Vagrantfile`, adjust `config.proxy.*`

7. Adjust `settings.yml` to your liking
8. Adjust `app-config.py` (the app's configuration) to your liking
9. Get the VM configured:

        vagrant up

10. On your host machine you can now connect to the VM's hosted app at [http://192.168.88.22]() (or the URL you have configured).

[vagrant]: http://www.vagrantup.com/downloads
[ansible]: http://docs.ansible.com/intro_installation.html#latest-releases-via-apt-ubuntu
[app]: https://github.com/chb/clinical-trials-app

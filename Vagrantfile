# -*- mode: ruby -*-

HOST_PORT = 8080
if (defined?(ip)).nil?
  IP_ADDRESS = "192.168.88.22"
end

Vagrant.configure(2) do |config|
  config.vm.hostname = "trials-app"
  config.vm.box = "ubuntu/trusty64"
  config.vm.network :private_network, :ip => IP_ADDRESS
  config.vm.network :forwarded_port, guest: 8000, host: HOST_PORT

  config.vm.provider :virtualbox do |v|
    v.name = "trials-app"
    v.memory = 2048
    v.cpus = 2
  end

  # use cachier plugin if available
  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box
  end
  
  # if you are behind a proxy
  if Vagrant.has_plugin?("vagrant-proxyconf")
    #config.proxy.http     = "http://yourproxy:8080"
    #config.proxy.https    = "http://yourproxy:8080"
    config.proxy.no_proxy = "localhost,127.0.0.1"
  end
  
  # play Ansible
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "playbook.yml"
    #ansible.verbose = "vvv"
    ansible.extra_vars = {
      vagrant_host: IP_ADDRESS
    }
  end
end

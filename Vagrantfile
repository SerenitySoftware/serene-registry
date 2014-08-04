def Kernel.is_windows?
    processor, platform, *rest = RUBY_PLATFORM.split("-")
    platform == 'mingw32'
end

Vagrant.configure("2") do |config|
    # Standard VM Settings
    config.vm.box = "hashicorp/precise64"

    if Kernel.is_windows?
        config.vm.network :public_network, :bridge => ENV['VAGRANT_BRIDGE']
    elsif ENV['VAGRANT_PRIVATE_IP'].nil?
        config.vm.network :private_network, type: :dhcp
    else
        config.vm.network :private_network, ip: ENV['VAGRANT_PRIVATE_IP']
    end

    config.vm.synced_folder ".", "/vagrant", type: "nfs"

    # Provisioning
    config.vm.provision :shell, :path => "dev/provision.sh"

    # SSH Configuration
    config.ssh.username = "vagrant"
    config.ssh.shell = "bash -l"
    config.ssh.keep_alive = true
    config.ssh.forward_agent = true
    config.ssh.forward_x11 = true
    config.vagrant.host = :detect

    # VirtualBox Provider
    config.vm.provider :virtualbox do |virtualbox, override|
        virtualbox.customize ["modifyvm", :id, "--name", "serene-registry"]
    end
end

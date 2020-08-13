def test_ssh_config_exists(host):
    home_path = "home"
    param_user = "linuxbrew"
    ssh_config = host.file("/{}/{}/.ssh/config".format(home_path, param_user))
    assert ssh_config.exists
    assert ssh_config.contains("StrictHostKeyChecking")
    assert ssh_config.contains("UserKnownHostsFile")

def test_ssh_folder(host):
    home_path = "home"
    param_user = "linuxbrew"
    ssh_config_folder = host.file("/{}/{}/.ssh".format(home_path, param_user))
    assert ssh_config_folder.is_directory
    assert ssh_config_folder.user == param_user
    assert ssh_config_folder.mode == 0o700


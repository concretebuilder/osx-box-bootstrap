def test_brew_packages_exist(host):
    packages = ['git', 'wget', 'hg', 'ansible', 'gdate', 'watchman', 'flow', 'tree', 'magick', 'gs', 'yarn', 'screen', 'python3']
    for package in packages:
      assert host.exists(package)

def test_ansible_cfg_exists(host):
    ansible_cfg = host.file("/home/linuxbrew/ansible.cfg")
    assert ansible_cfg.user == "linuxbrew"

def test_firebase_cli_exists(host):
    assert host.exists("firebase")

def test_bitrise_specific_folder(host):
    assert host.file("/home/linuxbrew/git").exists
    assert host.file("/home/linuxbrew/stepdir").exists
    assert host.file("/home/linuxbrew/deploy").exists
    assert host.file("Library/MobileDevice/Provisioning Profiles").exists
    assert host.file("/home/linuxbrew/profiles").exists
    assert host.file("/home/linuxbrew/build").exists
    assert host.file("/home/linuxbrew/bin").exists
    assert host.file("/home/linuxbrew/bitrise").exists
    assert host.file("/home/linuxbrew/bitrise/stepdata").exists
    assert host.file("/home/linuxbrew/bitrise/tools").exists

def test_pip_exists(host):
    assert host.exists("pip3")

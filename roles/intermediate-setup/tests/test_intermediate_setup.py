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
    folders = ["/home/linuxbrew/git",
    "/home/linuxbrew/stepdir","/home/linuxbrew/deploy",
    "Library/MobileDevice/Provisioning Profiles",
    "/home/linuxbrew/profiles",
    "/home/linuxbrew/build",
    "/home/linuxbrew/bin",
    "/home/linuxbrew/bitrise",
    "/home/linuxbrew/bitrise/stepdata",
    "/home/linuxbrew/bitrise/tools"]
    for folder in folders:
        assert host.file(folder).exists
def test_pip_exists(host):
    assert host.exists("pip3")

def test_brew_packages_exist(host):
    assert host.exists("git")
    assert host.exists("wget")
    assert host.exists("hg")
    assert host.exists("ansible")
    #checking coreutils
    assert host.exists("gdate")
    assert host.exists("watchman")
    assert host.exists("flow")
    assert host.exists("tree")
    assert host.exists("magick")
    assert host.exists("gs")
    assert host.exists("yarn")
    assert host.exists("screen")
    assert host.exists("python3")

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

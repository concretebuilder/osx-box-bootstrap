def test_brew_packages_exist(host):
    assert host.exists("git")
    assert host.exists("wget")
    assert host.exists("mercurial")
    assert host.exists("ansible")
    assert host.exists("coreutils")
    assert host.exists("watchman")
    assert host.exists("flow")
    assert host.exists("tree")
    assert host.exists("carthage")
    assert host.exists("imagemagick")
    assert host.exists("ghostscript")
    assert host.exists("yarn")
    assert host.exists("java")
    assert host.exists("screen")
    assert host.exists("readline")
    assert host.exists("python3")

def test_ansible_cfg_exists(host):
    ansible_cfg = host.file("/home/linuxbrew/ansible.cfg")
    assert ansible_cfg.user == "linuxbrew"

def test_firebase_cli_exists(host):
    assert host.exists("firebase")

def test_bitrise_specific_folder(host):
    assert host.file("/home/linuxbrew/git").exisßts
    assert host.file("/home/linuxbrew/stepdir").exists
    assert host.file("/home/linuxbrew/deploy").exists
    assert host.file("Library/MobileDevice/Provisioning Profiles").exists
    assert host.file("/home/linuxbrew/profiles").exists
    assert host.file("/home/linuxbrew/build").exists
    assert host.file("/home/linuxbrew/bin").exists
    assert host.file("/home/linuxbrew/bitrise").exists
    assert host.file("/home/linuxbrew/bitrise/stepdata").exists
    assert host.file("/home/linuxbrew/bitrise/tools").exists

def test_sync_tools_dir_exists(host):
    sync_tools_dir = host.file("/home/bitrise/tools/")
    assert sync_tools_dir.user == "linuxbrew"

def test_cmd_bridge_exists(host):
    bitrise_cli = host.file("/home/bitrise/tools/cmd-bridge/_scripts/install_launchctl_plist_for_current_user.sh")
    assert bitrise_cli.user == "vagrant"
    assert bitrise_cli.group == "staff"
    assert bitrise_cli.mode == 0o755

def test_xcode_stable_exists(host):
    assert host.exists("xcode-select")

def test_xcrun_simctl_exists(host):
    assert host.exists("xcrun")





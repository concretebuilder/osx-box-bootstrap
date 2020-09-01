def test_maxfiles_exists(host):
    maxfiles = host.file("/Library/LaunchDaemons/limit.maxfiles.plist")
    assert maxfiles.contains("root")
    assert maxfiles.user == "root"
    assert maxfiles.group == "wheel"
    assert maxfiles.mode == 644

def test_maxproc_exists(host):
    maxproc = host.file("/Library/LaunchDaemons/limit.maxproc.plist")
    assert maxproc.contains("root")
    assert maxproc.user == "root"
    assert maxproc.group == "wheel"
    assert maxproc.mode == 644

# Remote access scripts
def test_bitrise_folder_exists(host):
    bitrise = host.directory("/opt/bitrise")
    assert bitrise.user == "vagrant"
    assert bitrise.group == "wheel"
    assert bitrise.mode == 755

def test_ngrok_exists(host):
    ngrok = host.directory("/etc/ngrok")
    assert ngrok.user == "root"
    assert ngrok.group == "wheel"
    assert ngrok.mode == 755

def test_bootstrap_script_exists(host):
    bootstrap_script = host.directory("/opt/bitrise/bootstrap_remote_access.sh.tmpl")
    assert bootstrap_script.user == "vagrant"
    assert bootstrap_script.mode == 777

# Test ngrok
def test_ngrok_exists(host):
    assert host.exists("ngrok")
    nkgrok_bin = host.file("/usr/local/bin/ngrok")
    assert nkgrok_bin.mode == 700

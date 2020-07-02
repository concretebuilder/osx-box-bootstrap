def test_sshd_config_exists(host):
    assert host.file("/etc/ssh/sshd_config").exists

def test_sshd_config_is_valid(host):
    assert host.run("/usr/sbin/sshd -t -f /etc/ssh/sshd_config").succeeded

def test_sshd_config_permissions(host):
    sshd_config = host.file("/etc/ssh/sshd_config")
    assert sshd_config.user == "root"
    assert sshd_config.group == "root"
    assert sshd_config.mode == 0o644

def test_sshd_config_content(host):
    sshd_config = host.file("/etc/ssh/sshd_config")
    assert sshd_config.contains("Ansible managed")
    assert sshd_config.contains("bitrise overrides")
    assert sshd_config.contains("LogLevel                            VERBOSE")

import subprocess

def test_bitrise_cli_exists(host):
    bitrise_cli = host.file("/usr/local/bin/bitrise")
    assert bitrise_cli.user == "linuxbrew"
    assert bitrise_cli.group == "wheel"
    assert bitrise_cli.mode == 0o755

def test_bitrise_cli_version(host):
    actual = host.run("bitrise --version").stdout
    # be at least 1.46.0
    required = "1.46"
    assert actual >= required

def test_envman_is_installed(host):
    assert host.exists("/home/linuxbrew/.bitrise/tools/envman")

def test_stepman_is_installed(host):
    assert host.exists("/home/linuxbrew/.bitrise/tools/stepman")
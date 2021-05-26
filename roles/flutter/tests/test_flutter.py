def test_flutter_properly_installed(host):
    import platform
    assert "Flutter 1.26.0-17.8.pre" in host.run("{brew_path}/fvm flutter/bin/flutter --version".format(brew_path = '/usr/local/bin' if platform.system() == 'Darwin' else '/home/linuxbrew/.linuxbrew/bin')).stdout

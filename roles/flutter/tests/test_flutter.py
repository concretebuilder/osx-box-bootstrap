def test_flutter_properly_installed(host):
    assert "Flutter 1.22.6" in host.run("/usr/local/flutter/bin/flutter --version").stdout

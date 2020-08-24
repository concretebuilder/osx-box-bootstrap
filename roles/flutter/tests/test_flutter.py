def test_flutter_properly_installed(host):
    assert host.exists("flutter")
    assert host.run("flutter --version").stdout.contains('1.20.2')

def test_node_version_set_to_12(host):
    assert host.exists("node")
    assert host.run("node --version").stdout.startswith('v12')


def test_given_node_packages_are_installed(host):
    packages = ['ionic', 'cordova', 'appcenter']
    for package in packages:
      assert host.exists(package)

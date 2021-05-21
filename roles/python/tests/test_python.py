# Python tests
def test_if_python3_exists(host):
    assert host.exists("python3")
    assert host.run("python3 --version").stdout.startswith('Python 3')

# on linuxbrew the latest pip3 you can get is 2.18
# because the container was last updated in 2019
def test_if_pip3_exists(host):
    assert host.exists("pip3")
    assert host.run("pip3 --version").stdout.startswith('pip 18')

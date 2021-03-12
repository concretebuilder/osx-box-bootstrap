def test_bitrise_den_agent(host):
    bitrise_den_agent = host.file("/home/linuxbrew/bitrise-den-agent")
    assert bitrise_den_agent.user == "linuxbrew"
    assert bitrise_den_agent.group == "staff"
    assert bitrise_den_agent.mode == 0o755

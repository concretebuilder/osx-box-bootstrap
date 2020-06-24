def test_cmdline_tools_installed_and_available(host):
  cmd = host.run("env")
  assert "cmdline-tools" in cmd.stdout

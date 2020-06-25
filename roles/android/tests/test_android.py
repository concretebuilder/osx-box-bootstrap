def test_cmdline_tools_installed_and_available(host):
  cmd = host.run(". ~/profile.d/android.sh && env")
  assert "cmdline-tools" in cmd.stdout

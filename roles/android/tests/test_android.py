def test_sdkmanager_can_run_without_problem(host):
  assert host.run_expect([0], ". ~/profile.d/android.sh && sdkmanager --list")

def test_cmdline_tools_installed_and_available(host):
  cmd = host.run(". ~/profile.d/android.sh && env")
  assert "cmdline-tools" in cmd.stdout

def test_installed_sdkmanager_packages(host):
  variables = get_variables_from_defaults(host)
  for package in variables['sdkmanagerpackages']:
    assert host.run_expect([0], '. ~/profile.d/android.sh && ls $ANDROID_HOME/%s' % package.replace(";", "/"))

def get_variables_from_defaults(host):
  return host.ansible("include_vars", "file=../../../android/defaults/main.yml")['ansible_facts']

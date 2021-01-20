import unittest
import os
import sys
import testinfra.utils.ansible_runner

class TestBaseXcode(unittest.TestCase):
    def setUp(self):
        self.host = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_host('instance')
        self.vars = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_variables('instance')
        self.user_home = "/{}/{}/".format(self.vars['param_user_home'], self.vars['param_user'])

    def test_profiles(self):
        paths = ['.profiles/bitrise_profile', '.profiles/tools_profile', '.bashrc', '.zshrc', '.profile', '.bash_profile']

        for path in paths:
            self.assertTrue(self.host.file("{}{}".format(self.user_home, path)).is_file)

        self.assertTrue(self.host.file("{}.profiles".format(self.user_home)).is_directory)
        self.assertTrue(self.host.file("{}profile.d".format(self.user_home)).is_directory)

    def test_ruby(self):
        self.assertEqual(self.host.run('{}.rbenv/shims/ruby --version'.format(self.user_home)).rc, 0)

    def test_brew(self):
        brew = self.host.run('/usr/local/bin/brew --version')
        self.assertEqual(brew.rc, 0)
        self.assertIn('Homebrew 2', brew.stdout)

    @unittest.skipUnless(sys.platform == "darwin", 'xcode can be installed only on macos')
    def test_xcode(self):
        xcode = self.host.run('/usr/bin/xcodebuild -version')
        self.assertEqual(xcode.rc, 0)
        self.assertIn('Xcode ', xcode.stdout)
    
    def test_tmp_setup_basics(self):
        self.assertTrue(self.host.file('{}Desktop/debug.log'.format(self.user_home)).is_file)
        with self.host.sudo():
            self.assertTrue(self.host.file('/etc/sudoers').contains('vagrant ALL=(ALL) NOPASSWD: ALL'))
            self.assertIn('Developer mode is already enabled.', self.host.run("DevToolsSecurity").stdout)
            self.assertIn('Automatic check is off', self.host.run("softwareupdate --schedule").stdout)
            self.assertEqual(self.host.run('launchctl list | grep com.apple.apsd.plist').rc, 1)
            self.assertIn('assessments disabled', self.host.run("spctl --status").stdout)

    def test_cmd_bridge_installed(self):
        self.assertEqual(self.host.run('/usr/local/bin/cmd-bridge --version').rc, 0)


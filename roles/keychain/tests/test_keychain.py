import unittest
import os
import pytest

import testinfra.utils.ansible_runner

class TestIntermediateSetup(unittest.TestCase):
    def setUp(self):
        self.host = testinfra.utils.ansible_runner.AnsibleRunner(
            os.environ['MOLECULE_INVENTORY_FILE']).get_host('instance')

    @pytest.mark.parametrize('file, content', [
        "/Users/vagrant/Library/LaunchAgents/bitrise.io.tools.keychain-unlocker.plist", "bitrise.io.tools.keychain-unlocker",
        "/opt/bitrise/unlock_keychain.sh", "#!/bin/bash"
    ])
    def test_keychain_unlocker_files(self, file, content):
        file = self.host.file(file)

        assert file.exists
        assert file.contains(content)

    @pytest.mark.parametrize('file, content', [
        "/Users/vagrant/logs/bitrise.io.tools.keychain-unlocker.log", "Successfully unlocked login.keychain"
    ])
    def test_keychain_unlocker_has_run(self, file, content):
        file = host.file(file)

        assert file.exists
        assert file.contains(content)

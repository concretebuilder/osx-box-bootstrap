import unittest
import os
import testinfra.utils.ansible_runner

class TestBaseOS(unittest.TestCase):
    def test_spotlight_is_disabled(self):
        self.assertEqual(self.host.run("sudo launchctl list | grep -q com.apple.metadata.mds").rc, 0)

def test_brew_installed(host):
    assert host.run_expect([0], 'source ~/.bash_profile && brew --help')

def test_brew_core_sset_to_bitrise_io(host):
    brew_repository = host.run('source ~/.bash_profile && brew --repository').stdout.strip()
    brew_core_git_config_location = '{0}/Library/Taps/homebrew/homebrew-core/.git/config'.format(brew_repository)

    brew_core_git_config_file = host.file(brew_core_git_config_location)

    assert brew_core_git_config_file.exists
    assert brew_core_git_config_file.contains('github.com/bitrise-io/homebrew-core')

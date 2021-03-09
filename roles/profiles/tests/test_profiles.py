# Profiles tests

linux_home = "/home/linuxbrew/"

def test_profile_directories_exists(host):
    folders = [".profiles", "profile.d"]
    for folder in folders:
        bitrise = host.file(linux_home + folder)
        assert bitrise.is_directory
        assert bitrise.exists
        assert bitrise.user == "linuxbrew"

def test_profiles_exists(host):
    profiles = [
        ".profiles/bitrise_profile",
        ".profiles/tools_profile",
        ".bashrc",
        ".profile",
        ".bash_profile",
        ".zshrc"
    ]
    for profile in profiles:
        bitrise = host.file(linux_home + profile)
        assert bitrise.is_file
        assert bitrise.exists
        assert bitrise.user == "linuxbrew"


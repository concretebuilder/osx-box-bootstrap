# Xamarin tests
def test_xamarin_folders_exists(host):
    folder_path_base = "/home/linuxbrew/Library/Developer/"
    folders = ["Xamarin", "Xamarin/android-sdk-macosx", "Xamarin/android-sdk-macosx/ndk-bundle"]
    for folder in folders:
        bitrise = host.file(folder_path_base + folder)
        assert bitrise.is_directory
        assert bitrise.exists
        assert bitrise.user == "linuxbrew"

def test_config_folders_exists(host):
    folder_path_base = "/home/linuxbrew/"
    folders = ["bitrise/xamarin", ".local/share/Xamarin/Mono for Android", ".profiles"]
    for folder in folders:
        bitrise = host.file(folder_path_base + folder)
        assert bitrise.is_directory
        assert bitrise.exists
        assert bitrise.user == "linuxbrew"

def test_config_files_exist(host):
    folder_path_base = "/home/linuxbrew/"
    path_to_files = [".profiles/xamarin_profile", ".local/share/Xamarin/Mono for Android/debug.keystore"]
    for file in path_to_files:
        bitrise = host.file(folder_path_base + file)
        assert bitrise.is_file
        assert bitrise.exists
        assert bitrise.user == "linuxbrew"
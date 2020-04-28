-- Open vs4mac
tell application "Visual Studio"
	activate
end tell
-- Open up updates menu to download the files
tell application "System Events"
	tell process "Visual Studio"
		set frontmost to true
		name of every menu of menu bar 1
		click menu item "Check for Updates..." of menu "Visual Studio" of menu bar 1
	end tell
end tell
-- -- wait for downloads
delay 300
-- -- Click the install button
tell application "System Events"
	key code 48 using {shift down}
	key code 76
end tell
delay 5
-- -- Enter credentials
tell application "System Events"
	keystroke "vagrant"
	key code 76
end tell
-- -- Wait for the updates to install
delay 900

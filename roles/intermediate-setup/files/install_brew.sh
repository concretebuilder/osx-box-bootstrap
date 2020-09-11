#!/bin/bash

(
	echo
	echo "---> [install] Homebrew"
	echo '' | /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
	res_code=$?
	echo "---> [install] Homebrew [done]"

	exit $res_code
) 2>> ~/Desktop/debug.log 1>> ~/Desktop/debug.log
exit $?

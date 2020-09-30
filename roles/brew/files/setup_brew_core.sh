#!/bin/bash

set -e

source ~/.bash_profile

brew_repository=$(brew --repository)

rm -rf "$brew_repository/Library/Taps/homebrew"

git clone --bare https://github.com/bitrise-io/homebrew-core /var/tmp/homebrew-core

export HOMEBREW_CORE_GIT_REMOTE="/var/tmp/homebrew-core"

brew install a || true

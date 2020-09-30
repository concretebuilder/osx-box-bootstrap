#!/bin/bash

set -e

source ~/.bash_profile

brew_repository=$(brew --repository)

rm -rf "$brew_repository/Library/Taps/homebrew"

mkdir -p /opt/bitrise/mirrors/github.com/bitrise-io/

git clone --bare https://github.com/bitrise-io/homebrew-core /opt/bitrise/mirrors/github.com/bitrise-io/homebrew-core

export HOMEBREW_CORE_GIT_REMOTE="/opt/bitrise/mirrors/github.com/bitrise-io/homebrew-core"

brew install a || true

#!/bin/bash

set -e

source ~/.bash_profile

brew_repository=$(brew --repository)

rm -rf "$brew_repository/Library/Taps/homebrew"

export HOMEBREW_CORE_GIT_REMOTE="https://github.com/bitrise-io/homebrew-core"

brew install a || true

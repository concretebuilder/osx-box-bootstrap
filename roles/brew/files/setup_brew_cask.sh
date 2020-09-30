#!/bin/bash

set -e

source ~/.bash_profile

brew_repository=$(brew --repository)

git clone --bare https://github.com/bitrise-io/homebrew-cask /var/tmp/homebrew-cask

git clone /var/tmp/homebrew-cask "${brew_repository}/Library/Taps/homebrew/homebrew-cask"

#!/bin/bash

set -e

source ~/.bash_profile

brew_repository=$(brew --repository)

mkdir -p /opt/bitrise/mirrors/github.com/bitrise-io/

git clone --bare https://github.com/bitrise-io/homebrew-cask /opt/bitrise/mirrors/github.com/bitrise-io/

git clone /opt/bitrise/mirrors/github.com/bitrise-io/homebrew-cask "${brew_repository}/Library/Taps/homebrew/homebrew-cask"

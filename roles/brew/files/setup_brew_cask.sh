#!/bin/bash

set -e

source ~/.bash_profile

brew_repository=$(brew --repository)

git clone https://github.com/bitrise-io/homebrew-cask "${brew_repository}/Library/Taps/homebrew/homebrew-cask"

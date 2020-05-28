#!/bin/bash

rm -rf "$(brew --repository)/Library/Taps/homebrew"

export HOMEBREW_CORE_GIT_REMOTE="https://github.com/bitrise-io/homebrew-core"

brew install a || true

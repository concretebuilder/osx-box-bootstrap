#!/bin/bash

set -e

os="$(uname -s)"
if [[ "$os" == "Darwin" ]]; then
    echo "Installing Molecule and deps..."
    pip3 install molecule testinfra docker pytest &>"$BITRISE_DEPLOY_DIR"/pip_install.log
    molecule_version="$(molecule --version | sed -n 1p)"
    echo "Successfully installed $molecule_version"
else
    echo "Updating apt..."
    apt-get update &>/dev/null

    echo "Install apt dependencies..."
    apt-get install -y build-essential libssl-dev libffi-dev python-dev &>"$BITRISE_DEPLOY_DIR"/apt_install.log

    echo "Install pip3..."
    apt install -y python3-pip &>/dev/null
    pip install --upgrade pip &>/dev/null
    pip_version="$(pip --version | awk '{print $1, $2}')"
    echo "Installed $pip_version"

    pip install virtualenv molecule testinfra docker pytest &>"$BITRISE_DEPLOY_DIR"/pip_install.log
    molecule_version="$(molecule --version | sed -n 1p)"
    echo "Successfully installed $molecule_version"
fi
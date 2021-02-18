#!/usr/bin/env bash
set -e

# If .venv dir does not exist, create one
if [ !  -d "${PWD}/.venv" ]
then
    mkdir .venv
fi

# If virtual env does not exist, create one
if [ ! -f "${PWD}/.venv/bin/ativate " ]
then
    python3 -m venv "${PWD}/.venv"
fi

# Activate virtual env and add it to PATH, so we use pip3 from there
source "${PWD}/.venv/bin/activate"
export PATH="${PWD}/.venv/bin/:${PATH}"

# Set sane default versions
export ANSIBLE_LINT_VER="${ANSIBLE_LINT_VER:-4.2.0}"
export YAML_LINT_VER="${YAML_LINT_VER:-1.19.0}"

# Install in virtual env
pip3 install "ansible-lint==${ANSIBLE_LINT_VER}"
pip3 install "yamllint==${YAML_LINT_VER}"

yamllint --version
ansible-lint --version

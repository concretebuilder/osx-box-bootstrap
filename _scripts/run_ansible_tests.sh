#!/bin/bash

set -e

sudo apt install -y python3-pip

pip3 install molecule pytest testinfra  docker

cd roles/tests

molecule test

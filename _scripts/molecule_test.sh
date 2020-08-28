#!/bin/bash
set -eo pipefail

function run_test {
    molecule destroy -s "$1"
    molecule create -s "$1"
    molecule --debug converge -s "$1"
    molecule verify -s "$1"
    molecule destroy -s "$1"
}

run_test "${ROLE}" | tee "$BITRISE_DEPLOY_DIR/molecule.log"

#!/bin/bash
set -eo pipefail

molecule --debug test -s "${ROLE}" | tee "$BITRISE_DEPLOY_DIR/molecule.log"

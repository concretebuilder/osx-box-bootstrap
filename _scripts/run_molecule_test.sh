#!/bin/bash
set -eo pipefail

molecule test -s "${ROLE}" | tee "$BITRISE_DEPLOY_DIR/molecule.log"

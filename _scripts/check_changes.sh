#!/usr/bin/env/bash
set -euo pipefail
#
## Check what changed in the current commit/PR

file_list="$(git diff --name-only origin/master.."$BITRISE_GIT_BRANCH" | uniq)"
ansible_roles="$(ls ./roles)"

echo "Files changed: ${file_list}"

if [[ $file_list == *"roles"* ]]; then
  echo "You changed a role, we will run molecule tests."
  envman add --key DANGER_OUTPUT --value "You changed a role, we will run molecule tests."
  for role in ${ansible_roles}; do
    if [[ $file_list == *$role* ]]; then
      echo "WORKFLOW_TO_TRIGGER: test_${role}"
      envman add --key WORKFLOW_TO_TRIGGER --value "test_${role}"
    fi
  done
else
  echo "No changes in ansible"
  envman add --key DANGER_OUTPUT --value "No changes in ansible"
fi

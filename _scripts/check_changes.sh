#!/usr/bin/env/bash
set -euo pipefail
#
## Check what changed in the current commit/PR

file_list="$(git diff --name-only origin/master.."$BITRISE_GIT_BRANCH" | uniq)"
number_of_changed_roles="$(git diff --name-only origin/master.."$BITRISE_GIT_BRANCH" | grep "terraform/dc/" | cut -d/ -f3 | uniq | grep -c macstadium)" || true # Do not exit with 1 if we don't change anything under terraform/dc

echo "Files changed: ${file_list}"
echo "Number of roless changed: ${number_of_changed_roles}"

envman add --key CHANGED_TERRAFORM_CODE --value false
envman add --key MODULES_CHANGE --value false
envman add --key IS_ATL_PRIV --value false
envman add --key IS_VEG_PUB --value false
envman add --key IS_ATL3_PUB --value false
envman add --key IS_LAS1_PRV1 --value false
envman add --key IS_ATL01_PRV001 --value false

ansible_roles="$(ls ./roles)"

if [[ ${number_of_changed_roles} -gt 1 ]]; then
  echo "You should not change multiple roles at the same time"
  envman add --key DANGER_OUTPUT --value "You should not change multiple roles at the same time"
elif [[ $file_list == *"roles"* ]]; then
  echo "You changed a role, we will run molecule tests."
  envman add --key DANGER_OUTPUT --value "You changed a role, we will run molecule tests."
  for role in ${ansible_roles}; do
    if [[ $file_list == *$role* ]]; then
      echo "Changed role: ${role}"
      # envman add --key "${role}" --value true
    fi
  done
else
  echo "No changes in ansible"
  envman add --key DANGER_OUTPUT --value "No changes in ansible"
fi

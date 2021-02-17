#!/usr/bin/env/bash
set -euo pipefail
#
## Check what changed in the current commit/PR

file_list="$(git diff --name-only origin/master.."$BITRISE_GIT_BRANCH" | uniq)"
ansible_roles="$(ls ./roles)"
molecule_contents="$(ls ./roles/tests/molecule)"
# shellcheck disable=SC2207
available_tests=($(comm -12 <(printf '%s\n' "${ansible_roles[@]}" | LC_ALL=C sort) <(printf '%s\n' "${molecule_contents[@]}" | LC_ALL=C sort)))

echo "Files changed: ${file_list}"

number_of_changed_roles="$(git diff --name-only origin/master.."$BITRISE_GIT_BRANCH" | grep "roles" | cut -f1-2 -d"/" | uniq | grep -c roles)" || true # Do not exit with 1 if we don't change anything under roles
if [[ ${number_of_changed_roles} -gt 1 ]]; then
  echo "Please don't change multiple roles in one PR - Thanks, Build-Infra team"
  envman add --key DANGER_OUTPUT --value "Please don't change multiple roles in one PR - Thanks, Build-Infra team"

elif [[ $file_list == *"roles"* ]]; then
  echo "You changed a role, we will attempt to run molecule tests."
  envman add --key DANGER_OUTPUT --value "You changed a role, we will attempt to run molecule tests."
  for role in "${available_tests[@]}"; do
    if [[ $file_list == *$role* ]]; then
      echo "WORKFLOW_TO_TRIGGER: test_${role}"
      envman add --key WORKFLOW_TO_TRIGGER --value "test_${role}"
      envman add --key ROLE_CHANGED --value true
    fi
  done
else
  echo "No changes in ansible"
  envman add --key DANGER_OUTPUT --value "No changes in ansible"
fi

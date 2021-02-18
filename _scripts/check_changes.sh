#!/usr/bin/env/bash
set -euo pipefail
#
## Check what changed in the current commit/PR

file_list="$(git diff --name-only origin/master.."$BITRISE_GIT_BRANCH" | sort | uniq)"
sorted_file_list="$(echo "${file_list}" | grep "roles" | cut -f1-2 -d"/" | sort | uniq)"
ansible_roles="$(ls ./roles)"
molecule_contents="$(ls ./roles/tests/molecule)"
available_tests=$(comm -12 <(printf '%s\n' "${ansible_roles[@]}" | LC_ALL=C sort) <(printf '%s\n' "${molecule_contents[@]}" | LC_ALL=C sort))

available_workflows=("")
bitrise_readable_list=""

for file in $sorted_file_list; do
  if [[ $file == *"roles"* ]]; then
    envman add --key DANGER_OUTPUT --value "You changed a role, we will attempt to run molecule tests."
    processed_file="$(echo "${file}" | cut -f1-2 -d"/" | cut -f2 -d"/")"
    for test in $available_tests; do
      if [[ $test == "$processed_file" ]]; then
        available_workflows+=("test_${processed_file}")
        envman add --key TEST_IS_AVAILABLE --value true
      fi
    done
  fi
done

if [[ -n "${available_workflows[*]}" ]]; then
  bitrise_readable_list=$(sh -c 'IFS=$'\''\n'\'';echo "$*"' '' "${available_workflows[@]}")
  echo "${bitrise_readable_list}"
  envman add --key WORKFLOW_TO_TRIGGER --value "${bitrise_readable_list}"
fi

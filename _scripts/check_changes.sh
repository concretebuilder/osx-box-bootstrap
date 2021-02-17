#!/usr/bin/env/bash
set -euo pipefail
#
## Check what changed in the current commit/PR

file_list="$(git diff --name-only origin/master.."$BITRISE_GIT_BRANCH" | uniq)"
number_of_changed_roles="$(git diff --name-only origin/master.."$BITRISE_GIT_BRANCH" | grep "terraform/dc/" | cut -d/ -f3 | uniq | grep -c macstadium)" || true # Do not exit with 1 if we don't change anything under terraform/dc

echo "Files changed: ${file_list}"
echo "Number of DCs changed: ${number_of_changed_roles}"

envman add --key CHANGED_TERRAFORM_CODE --value false
envman add --key MODULES_CHANGE --value false
envman add --key IS_ATL_PRIV --value false
envman add --key IS_VEG_PUB --value false
envman add --key IS_ATL3_PUB --value false
envman add --key IS_LAS1_PRV1 --value false
envman add --key IS_ATL01_PRV001 --value false

if [[ ${number_of_changed_roles} -gt 1 ]]; then
  echo "You should not change multiple roles at the same time"
  envman add --key DANGER_OUTPUT --value "You should not change multiple datacenter configs"
elif [[ $file_list == *"vcsa"* ]]; then
  echo "You changed a module, that affects all datacenters, 
  Danger output would be long here, please see the build logs."
  envman add --key MODULES_CHANGE --value true
  envman add --key CHANGED_TERRAFORM_CODE --value true
  envman add --key DANGER_OUTPUT --value "You changed a module, that affects all datacenters, 
  Danger output would be long here, please see the build logs."
elif [[ "${file_list}" == *"terraform/dc"* ]]; then
  echo "Changed terraform code"
  envman add --key CHANGED_TERRAFORM_CODE --value true
  if [[ $file_list == *"macstadium-atl-priv-1"* ]]; then
    echo "Changed DC: ${file_list}"
    envman add --key IS_ATL_PRIV --value true
  elif [[ $file_list == *"macstadium-veg-pub-1"* ]]; then
    echo "Changed DC: ${file_list}"
    envman add --key IS_VEG_PUB --value true
  elif [[ $file_list == *"macstadium-atl-pub-1"* ]]; then
    echo "Changed DC: ${file_list}"
    envman add --key IS_ATL3_PUB --value true
  elif [[ $file_list == *"macstadium-LAS1-PRV1"* ]]; then
    echo "Changed DC: ${file_list}"
    envman add --key IS_LAS1_PRV1 --value true
  elif [[ $file_list == *"macstadium-ATL01-PRV001"* ]]; then
    echo "Changed DC: ${file_list}"
    envman add --key IS_ATL01_PRV001 --value true
  fi
else
  echo "No changes in Infrastructure"
  envman add --key DANGER_OUTPUT --value "No changes in Infrastructure"
fi

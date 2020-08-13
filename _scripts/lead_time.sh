#!/bin/bash

created_at=$(curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/repos/bitrise-io/osx-box-bootstrap/pulls?state=closed | jq '.[0].created_at')
envman add --key PR_CREATE_TIME --value "$created_at"
closed_at=$(curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/repos/bitrise-io/osx-box-bootstrap/pulls?state=closed | jq '.[0].closed_at')
envman add --key PR_CLOSED_TIME --value "$closed_at"

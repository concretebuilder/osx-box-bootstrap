msg = ''

fail("No issue number provided in the PR title! (format: `[PRJ-1234] This is a PR`)") if !github.pr_title.match(/\[\w{2,5}\-\d+\].*/)
fail("Please include a CHANGELOG entry.") if !git.modified_files.include?("CHANGELOG.md")
fail("Please change the date in bitrise_profile.") if !git.modified_files.include?("roles/profiles/files/bitrise_profile")

danger_output = (ENV['DANGER_OUTPUT']).to_s
unless danger_output.empty?
  msg << "```\n"
  msg << danger_output
  msg << "\n```\n\n"
end

markdown msg

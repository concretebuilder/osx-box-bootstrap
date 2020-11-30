#!/usr/bin/env python3
import subprocess
import re
import os
import sys

bashCommand = "xcrun xctrace list devices 2>&1 >/dev/null | grep iPhone"
process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True, env=os.environ.copy())
output, error = process.communicate()

lines = output.decode("utf-8").split("\n")
# Some devices contain both iOS and watchOS for some reason + ignoring SE simulators + removing empty lines
lines = [line for line in lines if "Watch" not in line and "iPhone SE" not in line and line]

if not lines:
  sys.exit(1)

r = re.compile("\(\d{1,2}\.\d{1,2}(\.\d{1,2})?\)")
device = sorted(lines, key=lambda x: re.search(r, x).group(), reverse=True)[1]
ios_version = re.search(r, device).group()[1:-1]
simulator_id = device.split()[-1][1:-1]
print(f"{ios_version} {simulator_id}")

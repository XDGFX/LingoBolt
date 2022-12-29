#!/usr/bin/env python3

# This script should:
# Read the stdin.
# Remove duplicates (leaving only the first occurrence of each line).
# Sort the lines.
# Print the result to stdout.

import sys

lines = sys.stdin.readlines()

lines = list(set(lines))
lines.sort()

for line in lines:
    print(line, end="")

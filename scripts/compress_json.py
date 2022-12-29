#!/usr/bin/env python3

import json
import os
import gzip

INPUT_FILE = os.path.join("..", "src", "french.json")
OUTPUT_FILE = os.path.join("..", "src", "french.json.gz")


def main():

    # Load the words JSON file
    with open(INPUT_FILE) as f:
        data = json.load(f)

    print(f"Loaded {len(data)} words from JSON file.")
    print(f"Original file size: {os.path.getsize(INPUT_FILE)} bytes")

    # Write the new JSON file
    with gzip.open(OUTPUT_FILE, "wt") as f:
        json.dump(data, f, ensure_ascii=False)

    print("Done.")
    print(f"New file size: {os.path.getsize(OUTPUT_FILE)} bytes")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import json
import sys
import os

WORD_LIST = os.path.join("..", "wordlists", "french.txt")
JSON_FILE = os.path.join("..", "src", "french.json")
OUTPUT_FILE = os.path.join("..", "src", "french_new.json")


def main():

    # Load all the words from the wordlist
    with open(WORD_LIST) as f:
        words = f.read().splitlines()

    print(f"Loaded {len(words)} words from wordlist.")

    # Load the words JSON file
    with open(JSON_FILE) as f:
        data = json.load(f)

    print(f"Loaded {len(data)} words from JSON file.")
    print(f"Original file size: {os.path.getsize(JSON_FILE)} bytes")

    # Remove all the words that are not in the wordlist
    data = [w for w in data if w["word"] in words]

    print(f"New word count: {len(data)}")

    # Sort the words alphabetically
    data = sorted(data, key=lambda k: k["word"])

    # Write the new JSON file as minified JSON
    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False)

    print("Done.")
    print(f"New file size: {os.path.getsize(OUTPUT_FILE)} bytes")


if __name__ == "__main__":
    main()

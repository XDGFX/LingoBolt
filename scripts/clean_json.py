#!/usr/bin/env python3

import json
import os

WORD_LIST = os.path.join("..", "wordlists", "fr.txt")
JSON_FILE = os.path.join("..", "src", "languages", "fr.json")
OUTPUT_FILE = os.path.join("..", "src", "languages", "french_new.json")


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

    # Sort the words alphabetically
    data = sorted(data, key=lambda k: k["word"])

    # Remove duplicate occurances of duplicate words
    data = [
        data[i]
        for i in range(len(data))
        if i == 0 or data[i]["word"] != data[i - 1]["word"]
    ]

    print(f"New word count: {len(data)}")

    # Write the new JSON file
    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False)

    print("Done.")
    print(f"New file size: {os.path.getsize(OUTPUT_FILE)} bytes")


if __name__ == "__main__":
    main()

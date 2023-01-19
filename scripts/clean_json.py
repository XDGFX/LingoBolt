#!/usr/bin/env python3

import json
import os
from tqdm import tqdm

_script_path = os.path.dirname(os.path.realpath(__file__))

WORD_LIST_DIR = os.path.join(_script_path, "..", "wordlists")
LANGUAGE_DIR = os.path.join(_script_path, "..", "src", "languages")


def clean(word_list, json_file):
    # Load all the words from the wordlist
    with open(word_list) as f:
        words = f.read().splitlines()

    print(f"Loaded {len(words)} words from wordlist.")

    # Load the words JSON file
    with open(json_file) as f:
        data = json.load(f)

    print(f"Loaded {len(data)} words from JSON file.")
    print(f"Original file size: {os.path.getsize(json_file)} bytes")

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
    with open(json_file, "w") as f:
        json.dump(data, f, ensure_ascii=False)

    print("Done.")
    print(f"New file size: {os.path.getsize(json_file)} bytes")


def main():
    # Loop over all json files in language dir
    for file in os.listdir(LANGUAGE_DIR):
        if not file.endswith(".json"):
            print(f"Skipping non json file: {file}")
            continue

        # Clean the file
        clean(
            os.path.join(WORD_LIST_DIR, file.replace(".json", ".txt")),
            os.path.join(LANGUAGE_DIR, file),
        )


if __name__ == "__main__":
    main()

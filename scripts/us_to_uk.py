#!/usr/bin/env python3

import json
import requests
import os
import re
from tqdm import tqdm

_script_path = os.path.dirname(os.path.realpath(__file__))

LANGUAGE_DIR = os.path.join(_script_path, "..", "src", "languages")
# OUTPUT_FILE = os.path.join(_script_path, "..", "src", "languages", "fr.json")

CHECK_KEYS = ["translation", "example_en", "tags", "part_of_speech", "gender"]

CONVERTER_JSON = "https://raw.githubusercontent.com/hyperreality/American-British-English-Translator/master/data/american_spellings.json"


def convert(sentence: str, converter: dict) -> str:
    # Split the sentence by spaces and punctuation
    words = re.split(r"(\s+|[,.;:!?])", sentence)

    # Loop through the words
    for i in range(len(words)):
        # If the word is in the dictionary, replace it
        if words[i] in converter:
            print(f"Converting {words[i]} to {converter[words[i]]}")
            words[i] = converter[words[i]]

    # Join the words back together
    return "".join(words)


def main():
    # Load the json into an object
    converter = requests.get(CONVERTER_JSON).json()

    # Loop over all json files in language dir
    for file in os.listdir(LANGUAGE_DIR):
        if not file.endswith(".json"):
            print(f"Skipping non json file: {file}")
            continue

        # Load the input file object
        obj = json.load(open(os.path.join(LANGUAGE_DIR, file), "r"))

        # Loop through the entries
        for i in tqdm(range(len(obj))):
            for check_key in CHECK_KEYS:
                if check_key in obj[i]:

                    # If the key is a string
                    if isinstance(obj[i][check_key], str):
                        obj[i][check_key] = convert(obj[i][check_key], converter)

                    # If it's a list, iterate through
                    elif isinstance(obj[i][check_key], list):
                        for j in range(len(obj[i][check_key])):
                            obj[i][check_key][j] = convert(
                                obj[i][check_key][j], converter
                            )

        # Write the new file
        with open(os.path.join(LANGUAGE_DIR, file), "w") as f:
            json.dump(obj, f, ensure_ascii=False)


if __name__ == "__main__":
    main()

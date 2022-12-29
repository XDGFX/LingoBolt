#!/usr/bin/env python3

import json
import typing
import time
import os

WORD_FILE = os.path.join("..", "wordlists", "french.txt")
OUTPUT_FILE = os.path.join("..", "src", "french.json")
BATCH = 3


def validate_word(word: str, input_obj: dict) -> bool:
    # Check that the input object matches the required format
    if not isinstance(input_obj, dict):
        print("Input must be a JSON object")
        return False

    required_keys = [
        "word",
        "translation",
        "example",
        "example_en",
        "emoji",
        "tags",
        "difficulty",
        "part_of_speech",
        "gender",
        "plural",
        "synonyms",
        "antonyms",
    ]
    for key in required_keys:
        if key not in input_obj:
            print(f"Missing required key: {key}")
            return False

    # Make sure the word is the same as the one we are adding
    if input_obj["word"] != word:
        print("Word does not match")
        return False

    # Make sure the tags are a list
    if not isinstance(input_obj["tags"], list):
        print("Tags must be a list")
        return False

    # Make sure the synonyms and antonyms are lists
    if not isinstance(input_obj["synonyms"], list):
        print("Synonyms must be a list")
        return False

    if not isinstance(input_obj["antonyms"], list):
        print("Antonyms must be a list")
        return False

    # Make sure the difficulty is a number
    if not isinstance(input_obj["difficulty"], int):
        print("Difficulty must be a number")
        return False

    return True


def get_response(word: str) -> typing.Union[None, dict]:
    response = input(f"{word}\n").strip().strip(",").strip()

    # The response should be a valid JSON object, in the format of:
    # {"word":"<word>","translation":"<translation>","example":"<example>","example_en":"<example_en>","emoji":"<emoji>","tags":"[<tags>]","difficulty":"<difficulty>","part_of_speech":"<part_of_speech>","gender":<gender>,"plural":<plural>,"synonyms":[<synonyms>],"antonyms":[<antonyms>]}
    try:
        input_obj = json.loads("[" + response + "]")

    except json.JSONDecodeError:
        print("Invalid JSON string")
        return None

    return input_obj


def main():
    # First we load all the words from WORD_FILE into a list
    with open(WORD_FILE, "r") as f:
        words = f.read().splitlines()

    # Then we open the output file, and check which words already exist
    with open(OUTPUT_FILE, "r") as f:
        existing_words = json.load(f)

    # The OUTPUT_FILE contains a list of objects, where the "w" parameter is the
    # word which we want to check.
    existing_words_list = [word["word"] for word in existing_words]

    # We then filter out the words which already exist in the output file
    words = [word for word in words if word not in existing_words_list]

    # We now iterate over every BATCH words and display them to the user.
    for i in range(0, len(words), BATCH):
        print("\n")

        start_time = time.time()

        # Get the next BATCH words
        next_words = words[i : i + BATCH]

        next_words_string = ", ".join(next_words)

        # Get the response from the user
        input_obj = get_response(next_words_string)

        # If the response is invalid, we skip this word
        if not input_obj:
            continue

        # If the response is valid, we validate it
        for word in next_words:
            # Find the object for this word
            word_obj = [x for x in input_obj if x["word"] == word]

            # If the word is not in the input object, we skip it
            if not word_obj:
                continue

            # Validate the object
            if not validate_word(word, word_obj[0]):
                continue

            # Add the word to the existing words
            existing_words.append(word_obj[0])

            # Update the output file
            with open(OUTPUT_FILE, "w") as f:
                json_string = json.dumps(existing_words, indent=4, ensure_ascii=False)
                f.write(json_string)

            print("\n\n")

        end_time = time.time()
        time_per_word = (end_time - start_time) / BATCH
        print(f"Time taken per word: {time_per_word} seconds")
        print(
            f"Estimated time remaining: {((len(words) - i) * time_per_word) / 60} minutes"
        )


if __name__ == "__main__":
    main()

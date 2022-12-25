#!user/bin/env python3

import json
import typing
import time

WORD_FILE = "french_words.json"
OUTPUT_FILE = "french.json"
BATCH = 3


def get_word(word: str) -> typing.Union[None, dict]:
    response = input(f"{word}:\n").strip().strip(",").strip()

    # The response should be a valid JSON object, in the format of:
    # {"word":"<word>","translation":"<translation>","example":"<example>","example_en":"<example_en>","emoji":"<emoji>","tags":"[<tags>]","difficulty":"<difficulty>","part_of_speech":"<part_of_speech>","gender":<gender>,"plural":<plural>,"synonyms":[<synonyms>],"antonyms":[<antonyms>]}
    try:
        input_obj = json.loads(response)

    except json.JSONDecodeError:
        print("Invalid JSON string")
        return None

    # Check that the input object matches the required format
    if not isinstance(input_obj, dict):
        print("Input must be a JSON object")
        return None

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
            return None

    # Make sure the word is the same as the one we are adding
    if input_obj["word"] != word:
        print("Word does not match")
        return None

    return input_obj


def main():

    # First we load all the words from WORD_FILE into a list
    with open(WORD_FILE, "r") as f:
        words = json.load(f)

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

        start_time = time.time()

        # Get the next BATCH words
        next_words = words[i : i + BATCH]

        for word in next_words:
            print(word, end=", ")

        print("\n")

        for word in next_words:
            obj = get_word(word)
            if obj is None:
                continue

            # Add the word to the existing words
            existing_words.append(obj)

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

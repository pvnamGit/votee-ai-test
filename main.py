import nltk
import requests
from nltk.corpus import words
import re


nltk.download("words")
nlkt_words = words.words()
exclude_words = set()

VOTEE_BASE_URL = "https://wordle.votee.dev:8000"

def validate_word(word, size, pattern):
    exclude_check = word not in exclude_words
    regex = f'{"".join(pattern)}'
    word_pattern = re.compile(regex)
    return len(word) == size and exclude_check and word_pattern.match(word)


def auto_guess_daily(size=5):
    pattern = ["." for _ in range(size)]

    while True:
        guessing_words = [
            word for word in nlkt_words if validate_word(word, size, pattern)
        ]
        guessing_word = guessing_words[0]
        feedbacks = requests.get(
            f"{VOTEE_BASE_URL}/daily", {"guess": guessing_word, "size": size}
        ).json()

        for feedback in feedbacks:
            if feedback["result"] == "correct":
                pattern[feedback["slot"]] = feedback["guess"]
            elif feedback["result"] == "absent":
                exclude_words.add(guessing_word)
            print(f'Pattern: {"".join(pattern)}')
        if "." not in pattern:
            print(f'Your word is {guessing_word}')
            break
        else:
            exclude_words.add(guessing_word)
            print(f'Wrong guess {guessing_word}')

def auto_guess_random(size=5, seed=None):
    pattern = ["." for _ in range(size)]

    while True:
        guessing_words = [
            word for word in nlkt_words if validate_word(word, size, pattern)
        ]
        guessing_word = guessing_words[0]
        feedbacks = requests.get(
            f"{VOTEE_BASE_URL}/random", {"guess": guessing_word, "size": size, "seed": seed}
        ).json()

        for feedback in feedbacks:
            if feedback["result"] == "correct":
                pattern[feedback["slot"]] = feedback["guess"]
            elif feedback["result"] == "absent":
                exclude_words.add(guessing_word)
            print(f'Pattern: {"".join(pattern)}')
        if "." not in pattern:
            print(f'Your word is {guessing_word}')
            break
        else:
            exclude_words.add(guessing_word)
            print(f'Wrong guess {guessing_word}')

def auto_guess_word(word):
    size = len(word)
    pattern = ["." for _ in range(size)]

    while True:
        guessing_words = [
            word for word in nlkt_words if validate_word(word, size, pattern)
        ]
        if not guessing_words:
            print("No matching words found. Exiting")
            break

        guessing_word = guessing_words[0]
        feedbacks = requests.get(
            f"{VOTEE_BASE_URL}/word/{word}", {"guess": guessing_word}
        ).json()

        for feedback in feedbacks:
            if feedback["result"] == "correct":
                pattern[feedback["slot"]] = feedback["guess"]
            elif feedback["result"] == "absent":
                exclude_words.add(guessing_word)
            print(f'Pattern: {"".join(pattern)}')
        if "." not in pattern:
            print(f'Your word is {guessing_word}')
            break
        else:
            exclude_words.add(guessing_word)
            print(f'Wrong guess {guessing_word}')

    #
if __name__ == '__main__':
    print('Choose an option:')
    print('1. Auto guess daily:')
    print('2. Auto guess random:')
    print('3. Auto guess word:')

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("AUTO GUESS DAILY")
        word_size = int(input("Enter size of the word: "))
        auto_guess_daily(word_size)
    elif choice == 2:
        print("AUTO GUESS RANDOM")
        word_size = int(input("Enter size of the word: "))
        seed = int(input("Enter seed: "))
        auto_guess_random(word_size, seed)
    elif choice == 3:
        print("AUTO GUESS WORD")
        word = input("Enter the specific word: ")
        auto_guess_word(word)
    else:
        print("Invalid choice")


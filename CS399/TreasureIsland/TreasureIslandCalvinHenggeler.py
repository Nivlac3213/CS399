""" CS 399 - Warmup - Playing around with a larger text file. """

import re
from time import process_time


def most_freq_word(list_of_words: [str]) -> (str, int):
    """
    Find the most frequently used word in the given word list
    :param list_of_words: list of words
    :return: most freq word, number of times the word is in the list
    """

    highest_occurrence = 0
    freq_word = ''
    unique_word_set = set(list_of_words)
    """
    freq_word = max(unique_word_set, key=list_of_words.count)
    highest_occurrence = list_of_words.count(freq_word)
    """
    for word in unique_word_set:
        occurrence = list_of_words.count(word)
        if occurrence > highest_occurrence:
            highest_occurrence = occurrence
            freq_word = word

    return freq_word, highest_occurrence


try:
    with open("treasure.txt") as file:
        text = file.read()
except IOError as err:
    print(err)
    exit(1)

regex = re.compile("[^a-zA-Z]")  # clean up, alt.: ''.join([c for c in text if c.isalpha() or c == " "])
clean_text = regex.sub(" ", text)  # replace all non alpha characters with a space
words = clean_text.lower().split()  # convert all uppercase characters to lower and split on spaces
t0 = process_time()
word, count = most_freq_word(words)
dt = process_time() - t0
print(f"Treasure Island has {len(words)} words.")
print(f"'{word}' is the most frequently used word. It appears {count} times.")
print(f"Processing: {dt} seconds")
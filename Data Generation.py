import random
import string
from random import choices
from difflib import SequenceMatcher


def main():
    seed_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=50))
    new_strings = generate_new_strings(seed_string)
    find_similar_strings(new_strings, seed_string)

def generate_new_strings(seed_string):

    population = [1, 2, 3, 4, 5, 6]
    weights = [0.7, 0.15, 0.1, 0.025, 0.02, 0.005]
    variations = choices(population, weights, k=100)

    new_strings = []
    for variation in range(len(variations)):
        new_string = ""
        for char in seed_string:
            if random.random() > 0.6:
                new_string = new_string + chr(ord(char) + variation)
            else:
                new_string = new_string + char
        new_strings.append(new_string)
    return new_strings

def find_similar_strings(new_strings, seed_string):
    safe_strings = []
    unsafe_strings = []
    for string in new_strings:
        if SequenceMatcher(None, string, seed_string).ratio() > 0.5:
            safe_strings.append(string)
        else:
            unsafe_strings.append(string)

    print(safe_strings)
    print("There are " + str(len(safe_strings)) + " safe strings")
    print(unsafe_strings)
    print("There are " + str(len(unsafe_strings)) + " unsafe strings")


if __name__ == '__main__':
    main()

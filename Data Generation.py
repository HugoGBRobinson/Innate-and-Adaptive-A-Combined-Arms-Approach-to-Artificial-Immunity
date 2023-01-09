import random
import string
from random import choices
from difflib import SequenceMatcher


def main():
    seed_string1 = "a" * 50
    seed_string2 = "9" * 50
    seed_string3 = "a"
    for i in range(50):
        seed_string3 = seed_string3 + str(ord(seed_string3[-1]) + 1)
    seed_string4 = ""
    seed_string5 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=50))

    strings_from_string1 = generate_new_strings(seed_string1)
    strings_from_string2 = generate_new_strings(seed_string2)
    strings_from_string3 = generate_new_strings(seed_string3)
    print(strings_from_string1)
    print(strings_from_string2)
    print(strings_from_string3)
    # new_strings = generate_new_strings(seed_string)
    # find_similar_strings(new_strings, seed_string)


def generate_new_strings(seed_string):
    population = [0, 1, 2, 3, 4, 5, 6]
    weights = [0.8, 0.15, 0.025, 0.02, 0.0025, 0.002, 0.005]
    new_strings = []
    for i in range(1000):
        variations = choices(population, weights, k=len(seed_string))
        new_string = ""
        for i in range(len(seed_string)):
            new_string = new_string + chr(ord(seed_string[i]) + variations[i])
        new_strings.append(new_string)
    return new_strings


def find_similar_strings(new_strings, seed_string):
    safe_strings = []
    unsafe_strings = []
    for string in new_strings:
        if SequenceMatcher(None, string, seed_string).ratio() > 0.1:
            safe_strings.append(string)
        else:
            unsafe_strings.append(string)

    print(safe_strings)
    print("There are " + str(len(safe_strings)) + " safe strings")
    print(unsafe_strings)
    print("There are " + str(len(unsafe_strings)) + " unsafe strings")


if __name__ == '__main__':
    main()

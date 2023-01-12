import random
import string
from random import choices
from difflib import SequenceMatcher
import csv
from functools import reduce


def main():
    seed_string1 = "a" * 50
    seed_string2 = "9" * 50
    seed_string3 = "a"
    for i in range(50):
        seed_string3 = seed_string3 + str(ord(seed_string3[-1]) + 1)
    seed_string4 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=50))

    attack_seed_string = "0" * 50
    attack_strings = generate_new_strings(attack_seed_string, 1000)
    for i in range(len(attack_strings)):
        attack_strings[i] = (attack_strings[i], True)

    strings_to_write_to_csv = [find_outlier_strings(generate_new_strings(seed_string1, 100000), seed_string1),
                               find_outlier_strings(generate_new_strings(seed_string2, 100000), seed_string2),
                               find_outlier_strings(generate_new_strings(seed_string3, 100000), seed_string3),
                               find_outlier_strings(generate_new_strings(seed_string4, 100000), seed_string4),
                               attack_strings]

    write_to_csv(reduce(lambda x, y: x + y, strings_to_write_to_csv))


def generate_new_strings(seed_string, no_of_strings):
    population = [0, 1, 2, 3, 4, 5, 6]
    weights = [0.8, 0.15, 0.025, 0.02, 0.0025, 0.002, 0.005]
    new_strings = []
    for i in range(no_of_strings):
        variations = choices(population, weights, k=len(seed_string))
        new_string = ""
        for i in range(len(seed_string)):
            new_string = new_string + chr(ord(seed_string[i]) + (1 * variations[i] if
                                                                 random.random() < 0.5 else -1 * variations[i]))
        new_strings.append(new_string)
    print("Strings generated")
    return new_strings


def find_outlier_strings(new_strings, seed_string):
    strings = []
    for string in new_strings:
        if SequenceMatcher(None, string, seed_string).ratio() > 0.2:
            strings.append((string, False))
        else:
            strings.append((string, True))

    return strings


def write_to_csv(strings):
    with open('Test_Data.csv', 'w', newline='') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['String', 'Attack'])
        for row in strings:
            csv_out.writerow(row)


if __name__ == '__main__':
    main()

import random
from random import choices


def main():
    new_strings = generate_new_strings("Hello")

def generate_new_strings(seed_string):
    population = [1, 2, 3, 4, 5, 6]
    weights = [0.7, 0.15, 0.1, 0.025, 0.02, 0.005]
    variations = choices(population, weights, k=100)

    new_strings = []
    for variation in range(len(variations)):
        new_string = ""
        for char in seed_string:
            if random.random() > 0.5:
                new_string = new_string + chr(ord(char) + variation)
            else:
                new_string = new_string + char
        new_strings.append(new_string)
    print(new_strings)

if __name__ == '__main__':
    main()

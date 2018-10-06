"""
Write a function that satisfies the following rules:

Return true if the string in the first element of the list contains all of the letters of the string in the second element of the list.
"""
from collections import Counter

def mutation(input_list):
    short, long = sorted(map(lambda l: l.lower(), input_list), key=lambda item: len(item))
    counter_short = Counter(short)
    counter_long = Counter(long)
    for letter in short:
        if letter not in long or counter_short[letter] != counter_long[letter]:
            return False
    return True


if __name__ == "__main__":
    print(mutation(["hello", "Hello"]))
    print(mutation(["hello", "hey"]))
    print(mutation(["Alien", "line"]))
    print(mutation(["aaaaa", "aaaa"]))
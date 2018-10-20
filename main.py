# -*- coding: utf-8 -*-
"""
Main Program
"""

def read_subword_file(filename):
    """
    read subword text
    """
    with open(filename, 'r') as fname:
        return list(map(lambda x: x.strip(), fname.readlines()))

def determine_word():
    """
    choose a typing word
    """
    word = 'cd'
    return word

def print_subword(word):
    """
    echo a typing subword and messages
    """
    message = 'Typing the Word.'
    print(message)
    print('>>> ' + word)

def main():
    """
    Main Process

    1. Determine a typing word
    2. Print the word
    3. (User) Typing
    4. Check
    """
    word = determine_word()
    print_subword(word)

if __name__ == '__main__':
    main()

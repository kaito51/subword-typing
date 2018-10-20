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

def determine_word(words):
    """
    choose a typing word
    """
    import random
    word = words[random.randrange(len(words))]
    return word

def print_subword(word):
    """
    echo a typing subword and messages
    """
    print('>>> ' + word)

def accept_the_answer():
    """
    Accept the  entered answer
    """
    answer = input()
    return answer

def check_the_answer(word, answer):
    """
    Check the answer
    """
    correct_or_not = True if word == answer else False

    return correct_or_not

def main(words):
    """
    Main Process

    1. Determine a typing word
    2. Print the word
    3. (User) Typing
    4. Check
    """
    word = determine_word(words)
    print_subword(word)

    while True:
        answer = accept_the_answer()
        if check_the_answer(word, answer):
            break
        else:
            print('incorrect')

def main_wrapper():
    """
    Loop main
    """
    words = read_subword_file('data/linux_command.txt')
    while True:
        main(words)

if __name__ == '__main__':
    main_wrapper()

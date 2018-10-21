# -*- coding: utf-8 -*-
"""
Main Program
"""
import scorer

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
    return words[random.randrange(len(words))]

def print_subword(word):
    """
    echo a typing subword and messages
    """
    print('>>> ' + word)

def accept_the_answer():
    """ Accept the  entered answer """
    answer = input()
    return answer

def is_continued(my_scorer):
    """ Check the end condition """
    check_flg = False if my_scorer.count >= 5 else True
    return check_flg

def check_the_answer(word, answer):
    """ Check the answer """
    correct_or_not = True if word == answer else False
    return correct_or_not

def main(words, my_scorer):
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
            my_scorer.increment_num_correct()
            my_scorer.increment_count()
            break
        else:
            my_scorer.increment_num_incorrect()
            print('incorrect')

def main_wrapper():
    """ Loop main """
    words = read_subword_file('data/linux_command.txt')
    my_scorer = scorer.Scorer()

    while is_continued(my_scorer):
        main(words, my_scorer)

    print(my_scorer.num_correct)
    print(my_scorer.num_incorrect)
    print(my_scorer.end_time())

if __name__ == '__main__':
    main_wrapper()

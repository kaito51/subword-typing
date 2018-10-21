# -*- coding: utf-8 -*-
"""
Evaluate Typing Skills
"""
import time

class Scorer:
    """
    scoler class
    """
    def __init__(self):
        self._count = 0
        self._num_correct = 0
        self._num_incorrect = 0
        self._start_time = time.time()

    @property
    def count(self):
        """ Counter """
        return self._count

    @property
    def num_correct(self):
        """ the number of correct answers """
        return self._num_correct

    @property
    def num_incorrect(self):
        """ the number of incorrect answers """
        return self._num_incorrect

    def increment_count(self):
        """ increment count """
        self._count += 1

    def increment_num_correct(self):
        """ increment num_correct """
        self._num_correct += 1

    def increment_num_incorrect(self):
        """ increment num_incorrect """
        self._num_incorrect += 1

    def end_time(self):
        """ Timer """
        return time.time() - self._start_time

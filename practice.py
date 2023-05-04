#!/usr/bin/env python3

import doctest
from typing import Tuple


def compare_two_ints(nums: Tuple):
    """
    Compares two integers.
    TODO: add more test cases.

    >>> compare_two_ints((12, 35))
    -1
    >>> compare_two_ints((5, 5))
    0
    """
    if nums[0] < nums[1]:
        return -1
    elif nums[1] < nums[0]:
        return -1
    return 0


def fibonacci(num: int):
    """
    Returns the nth number in the Fibonacci sequence (where n >= 0)
    https://en.wikipedia.org/wiki/Fibonacci_sequence

    These are unit tests:
    >>> [fibonacci(i) for i in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    >>> fibonacci(15)
    610
    """
    prev = 1
    cur = 0
    for _ in range(num):
        tmp = cur
        cur = cur + prev
        prev = tmp
    return cur


def is_palindrome(s: str):
    """
    Returns True if the input string is a palindrome (reads the same forward and backward)
    https://en.wikipedia.org/wiki/Palindrome

    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('to_ot')
    True
    >>> is_palindrome('abba')
    True
    >>> is_palindrome('ab')
    False
    >>> is_palindrome('aa')
    True
    >>> is_palindrome('abcba')
    True
    >>> is_palindrome('dabcba')
    False
    """
    for i in range(len(s) // 2):
        if s[i] != s[-1 - i]:
            return False
    return True


if __name__ == "__main__":
    doctest.testmod()  # This runs the doctests and prints any failures.

"""
Two strings are anagrams of each other if the letters of one string can be
rearranged to form the other string. Given a string, find the number of pairs
of substrings of the string that are anagrams of each other.
"""
from collections import defaultdict
from unittest import TestCase


def handshake(n):
    # https://mathworld.wolfram.com/HandshakeProblem.html
    # https://www.geeksforgeeks.org/number-of-handshakes-such-that-a-person-shakes-hands-only-once/
    if n == 0:
        return 0
    return (n - 1) + handshake(n - 1)


def sherlock_and_anagrams(word: str) -> int:
    anagrams = 0
    words = defaultdict(int)

    for start in range(len(word)):
        for stop in range(start + 1, len(word) + 1):
            sorted_ss = ''.join(sorted(word[start:stop]))
            words[sorted_ss] += 1

    for v in words.values():
        if v > 1:
            anagrams += handshake(v)

    return anagrams


class TestSherlockAndAnagrams(TestCase):
    def test_no_anagrams(self):
        self.assertEqual(0, sherlock_and_anagrams('abcd'))

    def test_simple_case(self):
        self.assertEqual(4, sherlock_and_anagrams('abba'))

    def test_simple_case2(self):
        self.assertEqual(3, sherlock_and_anagrams('ifailuhkqq'))

    def test_simple_case3(self):
        self.assertEqual(10, sherlock_and_anagrams('kkkk'))

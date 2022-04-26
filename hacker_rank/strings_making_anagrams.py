"""
A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

The student decides on an encryption scheme that involves two large strings. The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Determine this number.

Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

Example
a = 'cde'
b = 'dcf'
Delete e from a and f from b so that the remaining strings are cd and dc which are anagrams. This takes 2 character deletions.
"""
from collections import Counter
from unittest import TestCase


def make_anagram(a: str, b: str) -> int:
    # count the qty of each letter in both strings
    a_count = Counter(a)
    b_count = Counter(b)
    # subtract from a the qty found in b
    for k, v in b_count.items():
        a_count[k] -= v
    # count everything that is left in a, including negative occurrences
    return sum(map(abs, a_count.values()))


class TestMakeAnagram(TestCase):
    def test_simple_case(self):
        self.assertEqual(2, make_anagram('cde', 'dcf'))

    def test_simple_case2(self):
        self.assertEqual(4, make_anagram('cde', 'abc'))

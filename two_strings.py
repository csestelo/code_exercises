
#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#
from unittest import TestCase


def two_strings(s1: str, s2: str) -> str:
    for letter in s2:
        if letter in s1:
            return 'YES'
    return 'NO'


def improved_two_strings(s1: str, s2: str) -> str:
    # set offers O(1) access to its items, for membership tests
    all_letters = set(s1)

    for lt in s2:
        if lt in all_letters:
            return 'YES'
    return 'NO'


class TwoStringsTestCase(TestCase):
    def test_two_strings(self):
        self.assertEqual('YES', two_strings('hello', 'world'))
        self.assertEqual('NO', two_strings('hi', 'world'))
        self.assertEqual('NO', two_strings('wouldyoulikefries', 'abcabcabcabcabcabc'))
        self.assertEqual('YES', two_strings('hackerrankcommunity', 'cdecdecdecde'))
        self.assertEqual('YES', two_strings('jackandjill', 'wentupthehill'))
        self.assertEqual('NO', two_strings('writetoyourparents', 'fghmqzldbc'))
        self.assertEqual('YES', two_strings('aardvark', 'apple'))
        self.assertEqual('NO', two_strings('beetroot', 'sandals'))

    def test_improved_two_strings(self):
        self.assertEqual('YES', improved_two_strings('hello', 'world'))
        self.assertEqual('NO', improved_two_strings('hi', 'world'))
        self.assertEqual('NO', improved_two_strings('wouldyoulikefries', 'abcabcabcabcabcabc'))
        self.assertEqual('YES', improved_two_strings('hackerrankcommunity', 'cdecdecdecde'))
        self.assertEqual('YES', improved_two_strings('jackandjill', 'wentupthehill'))
        self.assertEqual('NO', improved_two_strings('writetoyourparents', 'fghmqzldbc'))
        self.assertEqual('YES', improved_two_strings('aardvark', 'apple'))
        self.assertEqual('NO', improved_two_strings('beetroot', 'sandals'))









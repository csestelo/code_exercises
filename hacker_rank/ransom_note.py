from collections import defaultdict
from unittest import TestCase
#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#


def check_magazine(magazine, note):
    magazine_words = defaultdict(int)

    for m_word in magazine.split():
        magazine_words[m_word] += 1

    for n_word in note.split():
        magazine_words[n_word] -= 1
        if magazine_words[n_word] < 0:
            return 'No'

    return 'Yes'


class RansomNote(TestCase):
    def test_check_magazine_case_1(self):
        self.assertEqual(
            "Yes",
            check_magazine(
                "give me one grand today night", "give one grand today"
            ),
        )

    def test_check_magazine_case_2(self):
        self.assertEqual(
            "No",
            check_magazine(
                "two times three is not four", "two times two is four"
            ),
        )

    def test_check_magazine_case_3(self):
        self.assertEqual(
            "No",
            check_magazine(
                "ive got a lovely bunch of coconuts", "ive got some coconuts"
            ),
        )

    def test_check_magazine_case_4(self):
        self.assertEqual(
            "No",
            check_magazine(
                "Attack at dawn", "attack at dawn"
            ),
        )

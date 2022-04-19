from functools import cmp_to_key
from unittest import TestCase

"""
Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array. The Player class is provided in the editor below. It has two fields:

1. name: a string.
2. score: an integer.
Given an array of "n" Player objects, write a comparator that sorts them in order of decreasing score. If 2 or more players have the same score, sort those players alphabetically ascending by name. To do this, you must create a Checker class that implements the Comparator interface, then write an int compare(Player a, Player b) method implementing the Comparator.compare(T o1, T o2) method. In short, when sorting in ascending order, a comparator function returns -1 if a < b, 0 if a == b, and 1 if a > b.

Declare a Checker class that implements the comparator method as described. It should sort first descending by score, then ascending by name. The code stub reads the input, creates a list of Player objects, uses your method to sort the data, and prints it out properly.
"""


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"Player(name={self.name}, score={self.score})"

    @staticmethod
    def comparator(a, b) -> int:
        if a.score == b.score:
            if a.name == b.name:
                return 0
            return -1 if a.name < b.name else 1
        else:
            return -1 if a.score > b.score else 1


def compare_scores(players: list[list[str]]) -> list[tuple]:
    data: list[Player] = [Player(name, score) for name, score in players]

    sorted_players = sorted(data, key=cmp_to_key(Player.comparator))
    return [(i.name, i.score) for i in sorted_players]


class TestPlayerComparator(TestCase):
    def test_simple_case(self):
        expected_result = [("Jones", 20), ("Smith", 20), ("Jones", 15)]
        input_data = [["Smith", 20], ["Jones", 15], ["Jones", 20]]
        self.assertEqual(expected_result, compare_scores(input_data))

    def test_simple_case2(self):
        expected_result = [
            ("aleksa", 150),
            ("amy", 100),
            ("david", 100),
            ("aakansha", 75),
            ("heraldo", 50),
        ]
        input_data = [
            ["amy", 100],
            ["david", 100],
            ["heraldo", 50],
            ["aakansha", 75],
            ["aleksa", 150],
        ]
        self.assertEqual(expected_result, compare_scores(input_data))

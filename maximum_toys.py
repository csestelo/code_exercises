"""
Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.
Note Each toy can be purchased only once.

Example:
prices = [1, 2, 3, 4]
k = 7

The budget is 7 units of currency. He can buy items that cost [1, 2, 3] for 6, or [3, 4] for 7 units. The maximum is 3 items.

Function Description

Complete the function maximumToys in the editor below. MaximumToys has the following parameter(s):
- int prices[n]: the toy prices
- int k: Mark's budget
Returns: int: the maximum number of toys
"""
from unittest import TestCase


def maximum_toys(prices: list[int], k: int) -> int:
    bought_toys = 0
    bought_toys_qtd = 0

    for price in sorted(prices):
        bought_toys += price
        if bought_toys <= k:
            bought_toys_qtd += 1
        else:
            break

    return bought_toys_qtd


class TestMaximumToys(TestCase):
    def test_simple_case(self):
        self.assertEqual(3, maximum_toys([1, 2, 3, 4], 7))

    def test_simple_case2(self):
        self.assertEqual(4, maximum_toys([1, 12, 5, 111, 200, 1000, 10], 50))

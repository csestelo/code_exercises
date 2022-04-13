"""
You are given  queries. Each query is of the form two integers described below:
-  1 x: Insert x in your data structure.
-  2 y: Delete one occurrence of y from your data structure, if present.
-  3 z: Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.

The queries are given in the form of a 2-D array "queries" of size "q" where "queries[i][0]" contains the operation, and "queries[i][1]" contains the data element.
"""
from collections import defaultdict
from unittest import TestCase

from hacker_rank.frequency_queries.big_input_result import expected_result


def update_frequencies(cont: defaultdict, from_: int, to: int) -> None:
    cont[from_] -= 1
    cont[to] += 1


def freq_query(queries: list[list[int]]) -> list[int]:
    freq_count = defaultdict(int)
    frequencies = defaultdict(int)
    result = []

    for q in queries:
        operation, data = q

        if operation == 1:
            freq_count[data] += 1

            update_frequencies(
                frequencies, freq_count[data] - 1, freq_count[data]
            )

        elif operation == 2:
            if freq_count[data] > 0:
                freq_count[data] -= 1

                update_frequencies(
                    frequencies, freq_count[data] + 1, freq_count[data]
                )

        elif operation == 3:
            result.append(int(frequencies[data] > 0))

    return result


class TestFrequencyQueries(TestCase):
    maxDiff = None

    def test_simple_case(self):
        queries = [[1, 1], [2, 2], [3, 2], [1, 1], [1, 1], [2, 1], [3, 2]]
        self.assertEqual([0, 1], freq_query(queries))

    def test_simple_case2(self):
        queries = [
            [1, 3],
            [2, 3],
            [3, 2],
            [1, 4],
            [1, 5],
            [1, 5],
            [1, 4],
            [3, 2],
            [2, 4],
            [3, 2],
        ]
        self.assertEqual([0, 1, 1], freq_query(queries))

    def test_big_input(self):
        queries = []
        with open("big_input_test.txt") as content:
            for line in content:
                queries.append(list(map(int, line.split())))

        self.assertEqual(expected_result, freq_query(queries))

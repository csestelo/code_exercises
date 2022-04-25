"""
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

Example
n = 10
queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
Queries are interpreted as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of k between the indices a and b inclusive:

index->	 1 2 3  4  5 6 7 8 9 10
        [0,0,0, 0, 0,0,0,0,0, 0]
        [3,3,3, 3, 3,0,0,0,0, 0]
        [3,3,3,10,10,7,7,7,0, 0]
        [3,3,3,10,10,8,8,8,1, 0]
The largest value is 10 after all operations are performed.
"""
import bisect
from collections import defaultdict
from unittest import TestCase


def array_manipulation(n: int, queries: list[list[int]]):
    result = defaultdict(int)
    highest_value = 0

    for i1, i2, value in queries:
        for i in range(i1, i2 + 1):
            result[i] += value
            if result[i] > highest_value:
                highest_value = result[i]

    return highest_value

# def array_manipulation2(n: int, queries: list[list[int]]):
#     all_items = array('Q', [0 for i_ in range(n)])
#     for i1, i2, value in queries:
#         for i in range(i1, i2):
#             all_items[i] += value
#
#     sorted_items = sorted(all_items)
#     return sorted_items[-1]


def array_manipulation2(n: int, queries: list[list[int]]):
    # ranges_i = [0, 1, 4, 6, 9, 10]
    ranges_i = [0]
    # ranges_v = {0: 0, 1: 3, 6: 8, 4: 10, 9: 1, 10: 0}
    ranges_v = defaultdict(int)
    highest_number = 0

    for start_i, end_i, value in queries:
        # inserir min na lista de ranges
        insert_start = bisect.bisect_left(ranges_i, start_i)
        if len(ranges_i) <= insert_start or ranges_i[insert_start] != start_i:
            ranges_i.insert(insert_start, start_i)

            # criar no ranges_v o valor do mín com valor do id anterior
            ranges_v[start_i] += ranges_v[ranges_i[insert_start - 1]]

        # inserir max + 1 na lista de ranges
        insert_end_i = bisect.bisect_left(ranges_i, end_i + 1)
        if len(ranges_i) <= insert_end_i or ranges_i[insert_end_i] != end_i + 1:
            ranges_i.insert(insert_end_i, end_i + 1)

            # criar no ranges_v o valor do max + 1 com valor do id anterior
            ranges_v[end_i + 1] += ranges_v[ranges_i[insert_end_i - 1]]

        # add valor atual (em ranges_v) a todos os itens de ranges_i entre o
        # valor min (incluindo ele) e o valor max (incluindo ele)
        for idx in range(insert_start, n):
            curr_item = ranges_i[idx]
            if curr_item >= ranges_i[insert_end_i]:
                break
            else:
                ranges_v[curr_item] += value
                curr_value = ranges_v[curr_item]
                if curr_value > highest_number:
                    highest_number = curr_value

    return highest_number


class TestArrayManipulation(TestCase):
    def test_simple_case(self):
        queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
        self.assertEqual(10, array_manipulation(10, queries))

    def test_simple_case2(self):
        queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
        self.assertEqual(200, array_manipulation(5, queries))

    def test_big_input(self):
        # it doesn't work, run forever =/
        with open("big_input.txt") as fp:
            queries = [map(int, line.split()) for line in fp]

        self.assertEqual(2497169732, array_manipulation(10000000, queries))


class TestArrayManipulation2(TestCase):
    def test_simple_case(self):
        queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
        self.assertEqual(10, array_manipulation2(10, queries))

    def test_simple_case2(self):
        queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
        self.assertEqual(200, array_manipulation2(5, queries))

    def test_big_input(self):
        # it doesn't work, run forever =/
        with open("big_input.txt") as fp:
            queries = [map(int, line.split()) for line in fp]

        self.assertEqual(2497169732, array_manipulation2(10000000, queries))

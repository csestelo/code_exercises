from unittest import TestCase

"""
# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. 
# You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.
"""


def minimum_swaps(q: list[int]):
    swaps = 0

    while True:
        inverted = False

        for idx, item in enumerate(q):
            if item == idx + 1:
                continue

            else:
                change_with_idx = item - 1
                other_item = q[change_with_idx]

                # one more swap
                swaps += 1

                # invert items to sort list
                q[idx], q[change_with_idx] = other_item, item

                inverted = True

        if not inverted:
            break

    print(swaps)
    return swaps


class TestMinimumSwaps(TestCase):
    def test_no_swaps(self):
        self.assertEqual(0, minimum_swaps([1, 2, 3, 4, 5]))

    def test_simple_case(self):
        self.assertEqual(3, minimum_swaps([1, 3, 5, 2, 4, 6, 7]))

    def test_more_complex_valid_scenario(self):
        self.assertEqual(3, minimum_swaps([4, 3, 1, 2]))

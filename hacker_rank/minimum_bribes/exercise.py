from unittest import TestCase

"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from  to . Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.
"""


def minimum_bribes(q: list[int]):
    bribes = 0
    q_len = len(q)

    while True:
        inverted = False

        for ix in range(q_len - 1):
            nex_idx = ix + 1
            cur_item = q[ix]
            nex_item = q[nex_idx]

            if cur_item - (ix + 1) > 2:
                print("Too chaotic")
                return "Too chaotic"

            if cur_item > nex_item:
                # one more bribe
                bribes += 1

                # invert items to get back to original order
                q[nex_idx], q[ix] = cur_item, nex_item

                inverted = True

        if not inverted:
            break

    print(bribes)
    return bribes


class TestMinimumBribes(TestCase):
    def test_no_bribes(self):
        self.assertEqual(0, minimum_bribes([1, 2, 3, 4, 5]))

    def test_simple_case(self):
        self.assertEqual(3, minimum_bribes([2, 1, 5, 3, 4]))

    def test_too_chaotic(self):
        self.assertEqual("Too chaotic", minimum_bribes([2, 5, 1, 3, 4]))

    def test_more_complex_valid_scenario(self):
        self.assertEqual(7, minimum_bribes([1, 2, 5, 3, 7, 8, 6, 4]))

    def test_super_complex_scenario(self):
        results = []
        with open("big_input_test.txt", encoding="utf-8") as content:
            for line in content:
                final_q = list(map(int, line.split()))
                results.append(minimum_bribes(final_q))

        self.assertEqual(
            [96110, "Too chaotic", "Too chaotic", 96319, 96323, 96058], results
        )

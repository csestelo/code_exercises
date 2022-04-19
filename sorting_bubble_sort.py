from unittest import TestCase

"""
Consider the following version of Bubble Sort:

for (int i = 0; i < n; i++) {
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
        }
    }
    
}
Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

1. Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
2. First Element: firstElement, where  is the first element in the sorted array.
3. Last Element: lastElement, where  is the last element in the sorted array.

"""


def bubble_sort(q: list[int]):
    swaps = 0
    q_len = len(q)

    while True:
        inverted = False

        for ix in range(q_len - 1):
            nex_idx = ix + 1
            cur_item = q[ix]
            nex_item = q[nex_idx]

            if cur_item > nex_item:
                # one more bribe
                swaps += 1

                # invert items to get back to original order
                q[nex_idx], q[ix] = cur_item, nex_item

                inverted = True

        if not inverted:
            break

    print(f'Array is sorted in {swaps} swaps. ')
    print(f'First Element: {q[0]}')
    print(f'Last Element: {q[-1]}')
    return swaps, q[0], q[-1]


class TestBubbleSort(TestCase):
    def test_no_swaps(self):
        self.assertEqual((3, 1, 6), bubble_sort([6, 4, 1]))

    def test_simple_case(self):
        self.assertEqual((3, 1, 3), bubble_sort([3, 2, 1]))

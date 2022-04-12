from unittest import TestCase

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def sum_rows(row_i, col_i, arr):
    top_row = arr[row_i][col_i] + arr[row_i][col_i + 1] + arr[row_i][col_i + 2]
    mid_row = arr[row_i + 1][col_i + 1]
    bottom_row = arr[row_i + 2][col_i] + arr[row_i + 2][col_i + 1] + \
                 arr[row_i + 2][col_i + 2]

    return top_row + mid_row + bottom_row


def hourglass_sum(arr):
    highest_sum = -63

    for row_i in range(4):
        for col_i in range(4):
            highest_sum = max(highest_sum, sum_rows(row_i, col_i, arr))

    return highest_sum


class HourglassTestCase(TestCase):
    def test_returns_highest_sum_case1(self):
        two_d_array = [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]
        ]

        self.assertEqual(19, hourglass_sum(two_d_array))

    def test_returns_highest_sum_case2(self):
        two_d_array = [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 9, 2, -4, -4, 0],
            [0, 0, 0, - 2, 0, 0],
            [0, 0, -1, -2, -4, 0]
        ]

        self.assertEqual(13, hourglass_sum(two_d_array))

    def test_returns_highest_sum_case3(self):
        two_d_array = [
            [-9, -9, -9, 1, 1, 1],
            [0, -9, 0, 4, 3, 2],
            [-9, -9, -9, 1, 2, 3],
            [0, 0, 8, 6, 6, 0],
            [0, 0, 0, -2, 0, 0],
            [0, 0, 1, 2, 4, 0]
        ]

        self.assertEqual(28, hourglass_sum(two_d_array))

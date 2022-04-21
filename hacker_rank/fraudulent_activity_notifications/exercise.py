"""
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to 2x the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days d and a client's total daily expenditures for a period of n days, determine the number of times the client will receive a notification over all n days.

Example:
expenditure = [10, 20, 30, 40, 50]
d = 3

On the first three days, they just collect spending data. At day 4, trailing expenditures are [10, 20, 30]. The median is 20 and the day's expenditure is 40. Because 40 >= 2 x 20, there will be a notice. The next day, trailing expenditures are [20, 30, 40] and the expenditures are 50. This is less than 2 x 30 so no notice will be sent. Over the period, there was one notice sent.

Note: The median of a list of numbers can be found by first sorting the numbers ascending. If there is an odd number of values, the middle one is picked. If there is an even number of values, the median is then defined to be the average of the two middle values. (Wikipedia)

Function Description

activityNotifications has the following parameter(s):

- int expenditure[n]: daily expenditures
- int d: the lookback days for median spending

Returns :: int: the number of notices sent
"""
import bisect
from itertools import islice
from unittest import TestCase


def get_median(items: list[int], middle_item: int, is_even: bool) -> float:
    if is_even:
        return (items[middle_item - 1] + items[middle_item]) / 2

    return items[middle_item]


def activity_notifications(expenditures: list[int], d: int) -> int:
    notifications = 0
    middle_item = d // 2
    is_even = d % 2 == 0

    last_exp = sorted(islice(expenditures, d))

    # checks the need for notification from day "d" onwards
    for i in range(d, len(expenditures)):
        curr_median = get_median(last_exp, middle_item, is_even)

        if expenditures[i] >= (2 * curr_median):
            notifications += 1

        del last_exp[bisect.bisect_left(last_exp, expenditures[i - d])]
        bisect.insort(last_exp, expenditures[i])

    return notifications


class TestActivityNotifications(TestCase):
    def test_simple_case(self):
        expenditures = [2, 3, 4, 2, 3, 6, 8, 4, 5]
        self.assertEqual(2, activity_notifications(expenditures, 5))

    def test_simple_case2(self):
        expenditures = [1, 2, 3, 4, 4]
        self.assertEqual(0, activity_notifications(expenditures, 4))

    def test_big_input(self):
        with open("big_input.txt") as content:
            expenditures = list(map(int, content.read().split()))

        self.assertEqual(633, activity_notifications(expenditures, 10000))

    def test_big_input2(self):
        with open("big_input_2.txt") as content:
            expenditures = list(map(int, content.read().split()))

        self.assertEqual(770, activity_notifications(expenditures, 9999))

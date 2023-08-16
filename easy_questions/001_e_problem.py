"""
The question is:
Return whether any two numbers from the list add up to k given a list of integers and a number k.
we will generate the lsit randomly.
"""

from random import choices
from random import randint

class TwoSum:
    """	Is a given number equal to the sum of two numbers in the given list or not?.

    Values ​​can be generated randomly or provided by the user.

    :param num: total value to be reached
    :type num: int, optional

    :param numbers: the list to be used to reach the total value
    :type numbers: list, optional
    """

    NUMBERS = list(range(15))

    def __init__(self, num=randint(0,15), numbers=choices(NUMBERS, k=4)):
        """Constructor method"""
        self.num = num
        self.numbers = numbers

    def check_sum(self):
        """checks to see if there are two numbers that sum up to the total value.

        :return: the presence of the total value
        :rtype: bool
        """
        cached_value = set()
        for val in self.numbers:
            if self.num - val in cached_value:
                return True
            cached_value.add(val)
            #print(cached_value)
        return False


test1 = TwoSum(13, [10, 15, 3, 7])

print(test1.num)
print(test1.numbers)
result = test1.check_sum()
print(result)
        
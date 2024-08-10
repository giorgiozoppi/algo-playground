"""This is the naive solution O(nlogn) for counting bit problem"""
from typing import List
class Solution:

    def countBits(self, n: int) -> List[int]:
        list_data = []
        for num in range(0, n+1):
            digits = self.compute_digit(num)
            list_data.append(digits)
        return list_data

    def compute_digit(self, num: int):
        count = 0
        if num == 0:
            return 0
        while num > 0:
            rest = num % 2
            num = num // 2
            if rest == 1:
                count = count + 1
        return count
#  https://leetcode.com/problems/fruit-into-baskets/

from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruits_count = defaultdict(int)
        res = 0

        left = 0
        for right, fruit in enumerate(fruits):
            fruits_count[fruit] += 1

            while len(fruits_count) > 2:
                fruits_count[fruits[left]] -= 1
                if fruits_count[fruits[left]] == 0:
                    del fruits_count[fruits[left]]
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
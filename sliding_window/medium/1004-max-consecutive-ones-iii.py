#  https://leetcode.com/problems/max-consecutive-ones-iii/

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_count = 0
        left = 0
        res = 0

        for right, num in enumerate(nums):
            if num == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
#  https://leetcode.com/problems/minimum-size-subarray-sum/

import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_res = math.inf

        cur = 0
        left = 0
        for right, val in enumerate(nums):
            cur += val
            while left <= right and cur >= target:
                min_res = min(min_res, right - left + 1)
                cur -= nums[left]
                left += 1
        return min_res if min_res < math.inf else 0
#  https://leetcode.com/problems/sliding-window-maximum/

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        left = 0
        for right, num in enumerate(nums):
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(right)

            if left > dq[0]:
                dq.popleft()

            if right + 1 >= k:
                res.append(nums[dq[0]])
                left += 1

        return res
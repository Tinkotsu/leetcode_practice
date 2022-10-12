#  https://leetcode.com/problems/3sum/

from typing import List, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            for reverse_pair in self._twoSum(nums, i+1, nums[i] * -1):
                if reverse_pair:
                    cur_res = (*reverse_pair, nums[i])
                    res.add(cur_res)
        
        return list(res)
    

    def _twoSum(self, nums: List[int], start: int, target: int) -> Tuple[int, int]:
        left, right = start, len(nums) - 1

        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum == target:
                yield (nums[left], nums[right])
                left += 1
                right -= 1
            elif two_sum > target:
                right -= 1
            else:
                left += 1
        return ()

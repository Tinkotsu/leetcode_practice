#  https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:  # skip duplicates
                continue
            if nums[i] > 0:  # there is no more negative numbers to the right, 0-sum is not possible
                break
            for reverse_pair in self._twoSum(nums, i+1, nums[i] * -1):
                triplet = [*reverse_pair, nums[i]]
                res.append(triplet)
        
        return res
    

    def _twoSum(self, nums: List[int], start: int, target: int) -> List[int]:
        left, right = start, len(nums) - 1

        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum == target:
                yield [nums[left], nums[right]]
                left += 1
                right -= 1
                while nums[left] == nums[left - 1] and left < right:  # skip duplicates
                    left += 1
            elif two_sum > target:
                right -= 1
            else:
                left += 1

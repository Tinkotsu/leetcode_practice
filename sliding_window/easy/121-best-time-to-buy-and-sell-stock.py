#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        left = right = 0
        
        while right < len(prices):
            if prices[right] < prices[left]:
                left += 1
                continue

            res = max(res, prices[right] - prices[left])
            right += 1
        
        return res
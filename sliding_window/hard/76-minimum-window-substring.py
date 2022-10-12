#  https://leetcode.com/problems/minimum-window-substring/

from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l_res = r_res = None
        chars_to_see = defaultdict(int)
        chars_seen = 0

        for char in t:
            chars_to_see[char] += 1
        
        left = 0
        for right, r_char in enumerate(s):
            if r_char in chars_to_see:
                chars_to_see[r_char] -= 1
                if chars_to_see[r_char] == 0:
                    chars_seen += 1
            
            while chars_seen == len(chars_to_see):
                if r_res is None or right - left < r_res - l_res:
                    r_res = right
                    l_res = left
                
                if s[left] in chars_to_see:
                    if chars_to_see[s[left]] == 0:
                        chars_seen -= 1
                    chars_to_see[s[left]] += 1
                
                left += 1
        
        return '' if r_res is None else s[l_res:r_res+1]
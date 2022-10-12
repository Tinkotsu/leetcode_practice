#  https://leetcode.com/problems/permutation-in-string/

from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars_to_see = defaultdict(int)
        chars_seen = 0

        for c in s1:
            chars_to_see[c] += 1
        
        left = 0
        for right, r_char in enumerate(s2):
            if r_char in chars_to_see:
                chars_to_see[r_char] -= 1
                if chars_to_see[r_char] == 0:
                    chars_seen += 1
            
            if right - left + 1 < len(s1):
                continue
            
            if chars_seen == len(chars_to_see):
                return True

            if s2[left] in chars_to_see:
                if chars_to_see[s2[left]] == 0:
                    chars_seen -= 1
                chars_to_see[s2[left]] += 1
            left += 1
            
        return False
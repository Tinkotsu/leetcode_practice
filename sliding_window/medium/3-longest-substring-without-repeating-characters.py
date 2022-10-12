#  https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = defaultdict(int)

        left = 0
        max_res = 0
        for right, char in enumerate(s):
            char_dict[char] += 1
            while right - left + 1 > len(char_dict):
                char_dict[s[left]] -= 1
                if char_dict[s[left]] == 0:
                    del char_dict[s[left]]
                left += 1
            max_res = max_res if max_res > len(char_dict) else len(char_dict)
        
        return max_res
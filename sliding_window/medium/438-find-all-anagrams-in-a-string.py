#  https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        anagram_dict = defaultdict(int)
        chars_seen = 0

        left = 0
        for i in p:
            anagram_dict[i] += 1

        for right, char in enumerate(s):
            if char in anagram_dict:
                anagram_dict[char] -= 1
                if anagram_dict[char] == 0:
                    chars_seen += 1
            
            if chars_seen == len(anagram_dict):
                res.append(left)

            if right - left + 1 == len(p):
                if s[left] in anagram_dict:
                    if anagram_dict[s[left]] == 0:
                        chars_seen -= 1
                    anagram_dict[s[left]] += 1
                left += 1
        
        return res
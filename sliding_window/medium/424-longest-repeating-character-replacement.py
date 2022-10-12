#  https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        left, result, max_repeat_letter_count = 0, 0, 0

        for right, right_char in enumerate(s):
            char_freq[right_char] += 1
            max_repeat_letter_count = max(char_freq[right_char], max_repeat_letter_count)

            if right - left + 1 - max_repeat_letter_count > k:
                char_freq[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
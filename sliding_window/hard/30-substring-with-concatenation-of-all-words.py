#  https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from collections import defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        words_freq = defaultdict(int)
        word_len = len(words[0])

        for word in words:
            words_freq[word] += 1
                
        for i in range(len(s)):
            words_seen_count = 0
            words_seen_dict = defaultdict(int)
            for j in range(len(words)):
                word_start_index = i + j * word_len
                word = s[word_start_index:word_start_index+word_len]

                if word not in words_freq:
                    break

                words_seen_dict[word] += 1
                if words_seen_dict[word] > words_freq[word]:
                    break

                if words_seen_dict[word] == words_freq[word]:
                    words_seen_count += 1
                if words_seen_count == len(words_freq):
                    res.append(i)
        
        return res

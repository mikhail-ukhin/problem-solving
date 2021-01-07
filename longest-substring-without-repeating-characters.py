# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        char_set = set()
        l, r = 0, 0

        while r < len(s):
            if not s[r] in char_set:
                char_set.add(s[r])
                r += 1
                max_len = max(len(char_set), max_len)
            else:    
                char_set.remove(s[l])
                l += 1

        return max_len
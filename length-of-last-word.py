# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a maximal substring consisting of non-space characters only.

# Example:

# Input: "Hello World"
# Output: 5

# O(m) - solution

class Solution(object):
    def lengthOfLastWord(self, s):
        if len(s) == 0: return 0
        
        word_len, word_started = 0, False
        
        for c in s[::-1]:
            if c == ' ' and not word_started: continue
            if c == ' ' and word_started: break
                
            word_started = True
            word_len += 1
            
        return word_len
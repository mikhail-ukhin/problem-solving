# Given an input string, reverse the string word by word.

# Example 1:

# Input: "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Note:

# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the reversed string.
 

class Solution(object):
    def reverseWords(self, s):
        if len(s) == 0: return s

        w = s.strip().split()
        i, l = 0, len(w) - 1

        while i <= l // 2:
            w[i], w[l - i] = w[l - i], w[i]
            i += 1

        return ' '.join(w)
# Given a string s, return the longest palindromic substring in s.

class Solution:
    # [ t,a, b, ,b ,a, c]
    # r a b c d d c b a x x
    # r a b b a x b a a b r
    def longestPalindrome(self, s: str) -> str:
        max_size = 0

        for i in range(len(s)):
            curr_len = self.get_palindrom_length(i, s)
            max_size = max(max_size, curr_len)

        return max_size


    def is_palindrome(self, s: str) -> bool:
        if not s: return False

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]: return False

            l += 1
            r -= 1

        return True    

    def get_palindrom_length(self, i: int, s: str) -> bool:
        l, r = i, i  
        max_l = 0
        sub = s[i]

        while l > -1 and r < len(s):
            if self.is_palindrome(sub):
                max_l = max(max_l, len(sub))
                l -= 1
                r += 1
                sub = s[l:r + 1]
            else:
                break    

        return max_l    


if __name__ == "__main__":
    s = Solution()
    r = s.longestPalindrome('bbbb')
    print(r)


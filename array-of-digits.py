# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

class Solution(object):
    def plusOne(self, digits):
        i, add_new_r = len(digits) - 1, False

        while i >= 0:
            new_digit = digits[i] + 1

            if new_digit < 10:
                digits[i] = new_digit
                break
            else:
                digits[i] = 0
                if i == 0:
                    add_new_r = True        
            i-= 1

        if add_new_r:
            digits = [1] + digits    

        return digits
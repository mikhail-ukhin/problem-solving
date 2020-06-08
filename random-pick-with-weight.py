# Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

# Note:

# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
# Example 1:

# Input: 
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
# Example 2:

# Input: 
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]

# Given an array w of positive integers, where w[i] describes the weight of index i, write a 
# function pickIndex which randomly picks an index in proportion to its weight.

# Note:

# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
# Example 1:

# Input: 
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
# Example 2:

# Input: 
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
# Explanation of Input Syntax:

# The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, 
# the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
import random


class Solution:

    __w_sum = []
    
    def __init__(self, weights):
        c_sum, i = 0, 0

        while i < len(weights):
            c_sum += weights[i]
            self.__w_sum[i] = c_sum
            i += 1

    def pickIndex(self):
        target = int(self.__w_sum[len(self.__w_sum) - 1] * random.random())
        i = 0

        while i < len(self.__w_sum):
            r = i
            i += 1

            if target < self.__w_sum[i]:
                return r
                
        return -1  


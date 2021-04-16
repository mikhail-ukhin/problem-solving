# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Find the kth positive integer that is missing from this array.

class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        c, i = 0, 0

        while i < len(arr):
            if i == 0 and arr[i] != 1: 
                c += (arr[i] - 1)
                if k <= c: return k
                    
            if i == len(arr) - 1: return arr[i] + (k - c)

            diff = arr[i + 1] - arr[i] - 1

            if (c + diff) >= k: return arr[i] + (k - c)
                

            if diff > 0: c += diff 
            i += 1

        return c
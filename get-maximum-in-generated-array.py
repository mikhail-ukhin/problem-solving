# Get Maximum in Generated Array

# You are given an integer n. An array nums of length n + 1 is generated in the following way:

#     nums[0] = 0
#     nums[1] = 1
#     nums[2 * i] = nums[i] when 2 <= 2 * i <= n
#     nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n

# Return the maximum integer in the array nums​​​.

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr = [0] * (n + 2)
        arr[1] = 1

        for i in range(2, n + 1):
            arr[i] = 

        return max(arr[:n + 1])

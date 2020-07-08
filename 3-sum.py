# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
    def threeSum(self, nums):
        if len(nums) < 3: return []

        nums = sorted(nums)
        i, j, k, trps = 0, 1, len(nums) - 1, set()

        while i < len(nums) - 2:
            if j >= k:
                i += 1
                j = i + 1
                k = len(nums) - 1

                if j == k: continue
            
            current_sum = nums[i] + nums[j] + nums[k]

            if current_sum == 0:
                trps.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
                
            elif current_sum > 0:
                k -= 1
            else:
                j += 1

        return list([[x[0], x[1], x[2]] for x in trps])     


if __name__ == "__main__":
     s = Solution()
     sums = s.threeSum([-2, -3, 0, 0, -2])

     print(sums)
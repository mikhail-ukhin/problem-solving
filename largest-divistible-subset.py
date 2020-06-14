# Largest Divisible Subset
# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

# Si % Sj = 0 or Sj % Si = 0.

# If there are multiple solutions, return any subset is fine.

# Example 1:

# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# Example 2:

# Input: [1,2,4,8]
# Output: [1,2,4,8]

def largestDivisibleSubset(self, nums):
    if not len(nums): return []
    
    sorted_nums = sorted(nums)
    counts = [[n] for n in sorted_nums]
    
    for i in range(len(sorted_nums)):
        for k in range(i):
            if sorted_nums[i] % sorted_nums[k] == 0 and len(counts[i]) < len(counts[k]) + 1:
                counts[i] = counts[k] + [sorted_nums[i]]
                
    return max(counts, key=len)

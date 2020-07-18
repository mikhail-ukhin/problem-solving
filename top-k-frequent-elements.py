# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Note:



import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}

        for n in nums:
            d[n] = d[n] + 1 if n in d else 1

        od = collections.OrderedDict(sorted(d.items(), key=lambda t: t[1], reverse=True))

        return list(od)[:k]
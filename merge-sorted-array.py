# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2. 

class Solution:
    def merge(self, nums1, m, nums2, n):
        p1, p2 = m - 1, n - 1

        for i in range(m + n - 1, -1, -1):
            if p1 < 0 or p2 < 0: break

            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
              
        while p2 > -1:
            nums1[i] = nums2[p2]
            i -= 1
            p2 -= 1    

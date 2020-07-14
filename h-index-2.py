# Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

# Example:

# Input: citations = [0,1,3,5,6]
# Output: 3 
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
#              received 0, 1, 3, 5, 6 citations respectively. 
#              Since the researcher has 3 papers with at least 3 citations each and the remaining 
#              two with no more than 3 citations each, her h-index is 3.
# Note:

# If there are several possible values for h, the maximum one is taken as the h-index.

class Solution(object):


    # O(n)
    def hIndex(self, citations):
        if not citations: return 0
        
        for i, c in enumerate(citations):
            n = len(citations) - i
            if c >= n: return n
            
        return 0    

    # O(log n)
    def hIndex2(self, citations):
        if not citations: return 0
        
        l = len(citations)
        begin, end = 0, l - 1

        while begin <= end:
            mid = begin + end // 2

            if mid + citations[mid] >= l:
                end = mid - 1
            else:
                begin = mid + 1

        return l - begin        
# Implement pow(x, n), which calculates x raised to the power n (xn).

# Example 1:

# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:

# Input: 2.10000, 3
# Output: 9.26100
# Example 3:

# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        if abs(n) == 1: return x if n > 0 else 1.0 / x

        results = {}
        cr, p = x, 1

        while p <= abs(n):
            results[p] = cr
            cr *= cr
            p *= 2

        p /= 2
        result, current_pow = results[p], p

        while current_pow < abs(n):
            p /= 2
            n_p = current_pow + p

            if n_p == abs(n):
                result *= results[p]
                break

            if n_p > abs(n): continue
            if n_p < abs(n): 
                result *= results[p]
                current_pow += p

        return result if n > 1 else 1.0 / result

if __name__ == "__main__":
    s = Solution()
    r = s.myPow(2, -2)
    print(r)
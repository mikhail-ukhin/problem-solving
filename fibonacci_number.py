class Solution:
    def fib(self, n: int) -> int:
        p1, p2, curr_n = 0, 1, 2
        res = p1 + p2

        if n == 0: return p1
        if n == 1: return p2

        while curr_n <= n:
            res = p1 + p2
            p1, p2 = p2, res
            curr_n += 1

        return res

        
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        total = m + n - 2
        def fact(x):
            for i in range(x - 1, 0, -1):
                x *= i
            return x
        return fact(total) // (fact(m - 1) * fact(n - 1))
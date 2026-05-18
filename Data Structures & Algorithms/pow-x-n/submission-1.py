class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1:
            return 1
        if x == 0:
            return 0
        if n == 1:
            return x
        multi = self.myPow(x, abs(n)//2) * self.myPow(x, abs(n)//2)
        if n % 2 == 1:
            multi *= x
        if n > 0:
            return multi
        else:
            return 1/multi
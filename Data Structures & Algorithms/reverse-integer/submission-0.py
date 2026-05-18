class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT, MIN_INT = 2**31 - 1, -2**31
        res = 0
        while x:
            digit = math.fmod(x, 10)
            x = int(x/10)
            if res > MAX_INT // 10 or (res == MAX_INT // 10 and digit > MAX_INT % 10):
                return 0
            elif res < MIN_INT // 10 or (res == MIN_INT // 10 and digit < MAX_INT % 10):
                return 0
            else:
                res = res * 10 + int(digit)
        return res
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l, r = 0, x
        while l < r:
            mid = (r - l) // 2 + l
            div = x // mid
            if div < mid:
                r = mid - 1
            else:
                l = mid + 1
        return l if l <= x // l else l - 1
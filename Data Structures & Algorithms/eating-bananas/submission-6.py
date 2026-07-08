class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l+r)//2
            t = 0
            for pile in piles:
                t += pile // mid
                if pile % mid != 0:
                    t += 1
            if t > h:
                l = mid + 1
            else:
                r = mid
        return l
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (r - l) // 2 + l  # banana eating rate
            hours = 0
            for pile in piles:
                if pile % mid > 0:
                    hours += 1
                hours += pile // mid
            if hours > h:
                l = mid + 1
            else:
                r = mid
        return l
            


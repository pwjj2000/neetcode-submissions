class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            print(l, r)
            mid = l + (r - l) // 2
            accum, d = 0, 0
            for w in weights:
                if accum + w > mid:
                    d += 1
                    accum = w
                else:
                    accum += w
            if accum: d += 1
            if d > days:
                l = mid + 1
            else:
                r = mid
            print(l, r, d)
        return l
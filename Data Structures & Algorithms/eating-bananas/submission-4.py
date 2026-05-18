class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            k = (left + right) // 2
            hours = 0
            for num in piles:
                hours += (num // k) + (0 if num % k == 0 else 1) 
            if hours <= h:
                right = k
            else:
                left = k + 1
        return left
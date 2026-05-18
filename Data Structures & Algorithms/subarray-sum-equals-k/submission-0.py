class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d  = {0 : 1}
        res, curr = 0, 0
        for num in nums:
            curr += num
            res += d.get(curr - k, 0)
            d[curr] = d.get(curr, 0) + 1
        return res
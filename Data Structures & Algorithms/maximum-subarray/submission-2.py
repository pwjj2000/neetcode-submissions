class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        curr = 0
        for n in nums:
            curr = max(0, curr)
            curr += n
            maxi = max(maxi, curr)
        return maxi
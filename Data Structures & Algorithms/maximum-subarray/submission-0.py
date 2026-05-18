class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxEndHere = maxi = nums[0]
        for i in range(1, len(nums)):
            maxEndHere = max(maxEndHere + nums[i], nums[i])
            maxi = max(maxi, maxEndHere)
        return maxi
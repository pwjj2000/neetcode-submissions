class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin, currMax = 1, 1
        result = nums[0]
        for num in nums:
            nextMax, nextMin = currMax * num, currMin * num
            currMax = max(nextMax, nextMin, num)
            currMin = min(nextMax, nextMin, num)
            result = max(result, currMax)
        return result
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i >= len(nums) - 2:
                dp[i] = nums[i]
            elif i == len(nums) - 3:
                dp[i] = dp[i + 2] + nums[i]
            else:
                dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])
        return max(dp[0], dp[1])
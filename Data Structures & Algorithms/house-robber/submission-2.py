class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n)
        for i in range(n - 1, -1, -1):
            if i + 3 < n:
                dp[i] = nums[i] + max(dp[i+2], dp[i+3])
            elif i + 2 < n:
                dp[i] = nums[i] + dp[i+2]
            else:
                dp[i] = nums[i]
        return max(dp[0: 2])
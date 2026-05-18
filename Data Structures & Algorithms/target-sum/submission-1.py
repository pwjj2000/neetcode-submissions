class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def helper(i, t):
            if (i, t) in dp:
                return dp[(i, t)]
            if i == len(nums):
                dp[(i, t)] = 1 if t == 0 else 0
                return dp[(i, t)]
            else:
                dp[(i, t)] = helper(i+1, t-nums[i]) + helper(i+1, t+nums[i])
                return dp[(i, t)]
        return helper(0, target)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        g = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if nums[i] + i >= g:
                g = i
        return g == 0
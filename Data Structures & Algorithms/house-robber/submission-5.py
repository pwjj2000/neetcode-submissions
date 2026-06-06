class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        for i in reversed(range(len(nums) - 2)):
            if i == len(nums) - 3:
                nums[i] += nums[i+2]
            else:
                nums[i] += max(nums[i+2], nums[i+3])
        return max(nums[0], nums[1])
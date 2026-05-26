class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        for i in range(len(nums)):
            if i - 1 >= 0:
                prefix[i] = nums[i-1] * prefix[i-1]
                suffix[len(nums)-i-1] = nums[len(nums)-i] * suffix[len(nums)-i]
        for i in range(len(nums)):
            prefix[i] *= suffix[i]
        return prefix
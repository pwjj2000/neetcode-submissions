class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            suffix[len(nums) - 1 - i] = suffix[len(nums) - i] * nums[len(nums) - i]
        for i in range(len(nums)):
            prefix[i] *= suffix[i]
        return prefix 

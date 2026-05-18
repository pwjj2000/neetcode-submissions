class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        remain = len(nums)
        for i in range(len(nums)):
            remain += i - nums[i]
        return remain
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n != i + 1:
                if nums[n - 1] == nums[i]:
                    return nums[i]
                nums[n - 1], nums[i] = n, nums[n - 1]
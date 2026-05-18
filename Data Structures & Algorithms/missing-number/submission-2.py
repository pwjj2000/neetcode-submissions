class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < len(nums) and i != nums[i]:
                a, b = nums[i], nums[nums[i]]
                nums[nums[i]] = a
                nums[i] = b
                print(nums)
        for i in range(len(nums)):
            if nums[i] < len(nums) and i != nums[i]:
                a, b = nums[i], nums[nums[i]]
                nums[nums[i]] = a
                nums[i] = b
                print(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
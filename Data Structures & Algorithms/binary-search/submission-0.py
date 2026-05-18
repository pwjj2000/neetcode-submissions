class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            index = (i + j) // 2
            if nums[index] == target:
                return index
            elif nums[index] < target:
                i = index + 1
            elif nums[index] > target:
                j = index - 1
        return -1
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        idx = 0
        for color in range(3):
            while count[color] > 0:
                nums[idx] = color
                idx += 1
                count[color] -= 1
        return nums

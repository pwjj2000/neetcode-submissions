class Solution:
    def jump(self, nums: List[int]) -> int:
        nums[-1] = 0
        smallest = float('inf')
        for i in range(len(nums)-2, -1, -1):
            smallest = 1 + min(smallest, nums[min(len(nums)-1, nums[i]+i)])
            nums[i] = smallest
        return min(smallest, nums[0])
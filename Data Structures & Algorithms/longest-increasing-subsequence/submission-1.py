class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        n = len(nums)
        stack = [(nums[i], i, 1) for i in range(n)]
        longest = 0
        while stack:
            val, index, length = stack.pop()
            if length > longest:
                longest = length
            for i in range(index + 1, n):
                if nums[i] > val:
                    stack.append((nums[i], i, length + 1))
        return longest
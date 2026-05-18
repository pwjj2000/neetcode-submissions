class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest, s = 0, set(nums)
        for num in s:
            if num - 1 not in s:
                n = num
                while n in s:
                    n += 1
                longest = max(longest, n - num)
        return longest

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, longest = set(nums), 0
        for c in s:
            if c - 1 not in s:
                i = c
                while i in s:
                    i += 1
                longest = max(longest, i - c)
        return longest 

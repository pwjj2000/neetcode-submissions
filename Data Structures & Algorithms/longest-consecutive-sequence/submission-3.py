class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in nums:
                l, n = 0, num
                while n in nums:
                    l += 1
                    n += 1
                if l > longest:
                    longest = l
        return longest

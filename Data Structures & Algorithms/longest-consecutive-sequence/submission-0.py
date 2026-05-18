class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxi = 0
        for num in nums:
            if num - 1 not in s:
                n = num
                while n in s:
                    n += 1
                maxi = max(maxi, n - num)
        return maxi

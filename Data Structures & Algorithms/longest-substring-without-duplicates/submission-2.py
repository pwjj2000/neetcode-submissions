class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left, right = 0, 0
        chars = set()
        while right < len(s):
            while right < len(s) and s[right] not in chars:
                chars.add(s[right])
                right += 1
            longest  = max(longest, right - left)
            while left < len(s) and right < len(s) and s[right] in chars:
                chars.remove(s[left])
                left += 1
        return longest


        
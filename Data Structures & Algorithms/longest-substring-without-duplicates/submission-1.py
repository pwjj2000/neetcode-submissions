class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r, chars = 0, 0, {}
        while l < len(s):
            while r < len(s) and s[r] not in chars.keys():
                chars[s[r]] = r
                r += 1
            longest = max(longest, len(chars.keys()))
            if r >= len(s):
                break
            while s[r] in chars.keys():
                chars.pop(s[l])
                l += 1
        return longest


        
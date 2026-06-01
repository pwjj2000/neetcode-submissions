class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        longest = 0
        l, r = 0, 0
        while r < len(s):
            while r < len(s) and s[r] not in curr:
                curr.add(s[r])
                r += 1
            if r - l > longest:
                longest = r - l
            while r < len(s) and s[r] in curr:
                curr.remove(s[l])
                l += 1
        return longest
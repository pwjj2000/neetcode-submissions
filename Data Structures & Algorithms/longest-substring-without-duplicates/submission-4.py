class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, chars = 0, set()
        longest = 0
        for r in range(len(s)):
            # Move l pointer until no more duplicates
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            
            # Add char in r pointer and update longest
            chars.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
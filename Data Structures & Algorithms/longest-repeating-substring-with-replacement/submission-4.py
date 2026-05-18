class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        count, max_freq_char_count = {}, 0
        for r in range(len(s)):
            count[s[r]]  = 1 + count.get(s[r], 0)
            max_freq_char_count = max(max_freq_char_count, count[s[r]])
            while r - l + 1 - max_freq_char_count > k:
                # max_freq_char remains the same even if l increments
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, d, longest = 0, defaultdict(int), 0
        max_f = 0
        for r in range(len(s)):
            # Update most frequent char count
            d[s[r]] += 1
            max_f = max(max_f, d[s[r]])

            # Move left pointer until k not exceeded
            while r - l + 1 - max_f > k:
                d[s[l]] -= 1
                l += 1

            # Update longest
            longest = max(longest, r - l + 1)
        return longest
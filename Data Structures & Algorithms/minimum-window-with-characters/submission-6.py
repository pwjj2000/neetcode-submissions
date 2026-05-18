class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains(s_count: list, t_count: list) -> bool:
            for i in range(52):
                if s_count[i] < t_count[i]:
                    return False
            return True
        
        s_count, t_count = [0] * 52, [0] * 52
        for c in t:
            if c == c.lower():
                t_count[ord(c) - ord('a')] += 1
            else:
                t_count[ord(c) - ord('A') + 26] += 1

        res = ""
        l = 0
        for r in range(len(s)):
            if s[r] == s[r].lower():
                s_count[ord(s[r]) - ord('a')] += 1
            else:
                s_count[ord(s[r]) - ord('A') + 26] += 1

            while contains(s_count, t_count):
                if not res or r - l + 1 < len(res):
                    res = s[l:r+1]
                if s[l] == s[l].lower():
                    s_count[ord(s[l]) - ord('a')] -= 1
                else:
                    s_count[ord(s[l]) - ord('A') + 26] -= 1
                l += 1
        return res
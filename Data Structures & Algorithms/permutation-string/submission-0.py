class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Chars, s2Chars = [0] * 26, [0] * 26 
        matches = 0
        for c in s1:
            s1Chars[ord(c) - ord('a')] += 1
        for c in s2[:len(s1)]:
            s2Chars[ord(c) - ord('a')] += 1
        for i in range(len(s1Chars)):
            if s1Chars[i] == s2Chars[i]:
                matches += 1
        l, r = 0, len(s1) - 1
        while r < len(s2):
            if matches == 26:
                return True
            prev = s2[l]
            if s2Chars[ord(prev) - ord('a')] == s1Chars[ord(prev) - ord('a')]:
                matches -= 1
            s2Chars[ord(prev) - ord('a')] -= 1
            if s2Chars[ord(prev) - ord('a')] == s1Chars[ord(prev) - ord('a')]:
                matches += 1
            if r + 1 >= len(s2):
                break
            next = s2[r + 1]
            if s2Chars[ord(next) - ord('a')] == s1Chars[ord(next) - ord('a')]:
                matches -= 1
            s2Chars[ord(next) - ord('a')] += 1
            if s2Chars[ord(next) - ord('a')] == s1Chars[ord(next) - ord('a')]:
                matches += 1
            l += 1
            r += 1
        return False
        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1, freq2 = [0] * 26, [0] * 26
        for c in s1:
            freq1[ord(c) - ord('a')] += 1
        for i in range(len(s1)):
            freq2[ord(s2[i]) - ord('a')] += 1
        same = 0
        for i in range(26):
            if freq1[i] == freq2[i]:
                same += 1
        if same == 26:
            return True
        for i in range(len(s1), len(s2)):
            if freq1[ord(s2[i - len(s1)]) - ord('a')] == freq2[ord(s2[i - len(s1)]) - ord('a')]:
                same -= 1
            if freq1[ord(s2[i]) - ord('a')] == freq2[ord(s2[i]) - ord('a')]:
                same -= 1
            freq2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            freq2[ord(s2[i]) - ord('a')] += 1
            if freq1[ord(s2[i - len(s1)]) - ord('a')] == freq2[ord(s2[i - len(s1)]) - ord('a')]:
                same += 1
            if freq1[ord(s2[i]) - ord('a')] == freq2[ord(s2[i]) - ord('a')]:
                same += 1
            if same == 26:
                return True
        return False
        
        
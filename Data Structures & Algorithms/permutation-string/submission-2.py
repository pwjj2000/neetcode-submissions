class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1, count2 = [0] * 26, [0] * 26
        for c in s1:
            count1[ord(c) - ord('a')] += 1
        same = 0
        for i in range(26):
            if count1[i] == count2[i]:
                same += 1
        l = 0
        for r in range(len(s2)):
            if count1[ord(s2[r]) - ord('a')] == count2[ord(s2[r]) - ord('a')]:
                same -= 1
            count2[ord(s2[r]) - ord('a')] += 1
            if count1[ord(s2[r]) - ord('a')] == count2[ord(s2[r]) - ord('a')]:
                same += 1

            if r >= len(s1):
                if count1[ord(s2[l]) - ord('a')] == count2[ord(s2[l]) - ord('a')]:
                    same -= 1
                count2[ord(s2[l]) - ord('a')] -= 1
                if count1[ord(s2[l]) - ord('a')] == count2[ord(s2[l]) - ord('a')]:
                    same += 1
                l += 1

            if same == 26: return True
        return False
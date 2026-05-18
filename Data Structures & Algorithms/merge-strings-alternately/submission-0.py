class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer, m, n, i = '', len(word1), len(word2), 0
        while i < m or i < n:
            if i < m:
                answer += word1[i]
            if i < n:
                answer += word2[i]
            i += 1
        return answer
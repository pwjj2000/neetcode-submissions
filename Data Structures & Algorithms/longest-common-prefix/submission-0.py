class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            idx, goNext = 0, False
            for idx in range(min(len(strs[i]), len(prefix))):
                if strs[i][idx] != prefix[idx]:
                    prefix = prefix[:idx]
                    goNext = True
                    break
            if not goNext and len(strs[i]) < len(prefix):
                prefix = strs[i]
        return prefix
                
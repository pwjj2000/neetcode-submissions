class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            t = tuple(count)
            if t not in d:
                d[t] = []
            d[t].append(s)
        return list(d.values()) 

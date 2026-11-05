class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            letter = [0] * 26
            for c in s:
                letter[ord(c)-97] += 1
            d[tuple(letter)].append(s)
        return list(d.values())
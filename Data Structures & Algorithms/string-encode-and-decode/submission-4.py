class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans += str(len(s)) + '#' + s
        return ans

    def decode(self, s: str) -> List[str]:
        curr = ''
        i = 0
        ans = []
        while i < len(s):
            if s[i] in '0123456789':
                curr += s[i]
                i += 1
            elif s[i] == '#':
                l = int(curr)
                ans.append(s[i+1:i+l+1])
                i += l + 1
                curr = ''
        return ans
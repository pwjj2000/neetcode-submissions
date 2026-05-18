class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for string in strs:
            l = len(string)
            s += str(l) + '#' + string
        return s

    def decode(self, s: str) -> List[str]:
        num, res = '', []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num += s[i]
                i += 1
            elif s[i] == '#':
                n = int(num)
                res.append(s[i + 1: i + 1 + n])
                i += 1 + n
                num = ''
        return res
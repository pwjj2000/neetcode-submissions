class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            encoded_string += str(len(s)) + '#' + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = []
        i, length = 0, ''
        while i < len(s):
            if s[i] == '#':
                strs.append(s[i + 1: i + 1 + int(length)])
                i += 1 + int(length)
                length = ''
            else:
                length += s[i]
                i += 1
        return strs

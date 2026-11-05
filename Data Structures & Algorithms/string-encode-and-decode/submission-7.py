class Solution:

    def encode(self, strs: List[str]) -> str:
        s = []
        for string in strs:
            s.append(str(len(string)))
            s.append("#")
            s.append(string)
        return "".join(s)

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0
        l = ""
        while i < len(s):
            if s[i] == "#":
                strings.append(s[i+1:i+1+int(l)])
                i = i + 1 + int(l)
                l = ""
            else:
                l += s[i]
                i += 1
        return strings
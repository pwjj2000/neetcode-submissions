class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(['(' + s + ')' for s in strs])
    def decode(self, s: str) -> List[str]:
        ans = []
        count = 0
        string = ''
        for c in s:
            if c == '(':
                count += 1
                if count == 1:
                    continue
            elif c == ')':
                count -= 1
            if count > 0:
                string += c
            else:
                ans.append(string)
                string = ''
        return ans


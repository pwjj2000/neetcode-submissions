class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, curr = [], []
        def backtrack(l, r):
            if l == r == n:
                res.append("".join(curr))
                return

            if l < n:
                curr.append("(")
                backtrack(l+1, r)
                curr.pop()
            if r < l:
                curr.append(")")
                backtrack(l, r+1)
                curr.pop()
        backtrack(0, 0)
        return res
            
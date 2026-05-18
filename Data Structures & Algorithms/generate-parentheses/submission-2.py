class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parantheses = []
        def backtrack(openN, closeN, curr):
            if openN == closeN == n:
                parantheses.append(curr)
                return
            if openN < n:
                backtrack(openN + 1, closeN, curr + "(")
            if closeN < openN:
                backtrack(openN, closeN + 1, curr + ")")
        backtrack(0, 0, "")
        return parantheses
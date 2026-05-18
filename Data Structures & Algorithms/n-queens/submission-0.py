class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posd, negd = set(), set(), set()
        res = []
        board = [['.'] * n for _ in range(n)]
        def backtrack(i):
            if i == n:
                c = [''.join(row) for row in board]
                res.append(c)
                return
            for j in range(n):
                if j in cols or i-j in negd or i+j in posd:
                    continue
                board[i][j] = 'Q'
                cols.add(j)
                posd.add(i+j)
                negd.add(i-j)
                backtrack(i+1)
                board[i][j] = '.'
                cols.remove(j)
                posd.remove(i+j)
                negd.remove(i-j)
        backtrack(0)
        return res
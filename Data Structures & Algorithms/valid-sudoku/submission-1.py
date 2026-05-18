class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s = set()
            for cell in row:
                if cell == '.':
                    continue
                if cell in s:
                    return False
                s.add(cell)
        for j in range(9):
            s = set()
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        d = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in d[(i // 3, j // 3)]:
                    return False
                d[(i // 3, j // 3)].add(board[i][j])
        return True
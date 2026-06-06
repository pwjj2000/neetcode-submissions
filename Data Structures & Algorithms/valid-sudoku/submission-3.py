class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    print('row')
                    return False
                s.add(board[i][j])
        for j in range(9):
            s = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    print('col')
                    return False
                s.add(board[i][j])
        for b in range(9):
            s = set()
            for i in range(b // 3 * 3, b // 3 * 3 +3):
                for j in range(b % 3 * 3, b % 3 * 3 + 3):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in s:
                        print(i,j)
                        return False
                    s.add(board[i][j])
        return True

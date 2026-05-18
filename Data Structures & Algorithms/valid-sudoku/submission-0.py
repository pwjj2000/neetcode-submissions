class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in visited:
                    visited.add(board[i][j])
                else:
                    return False
        for j in range(9):
            visited = set()
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in visited:
                    visited.add(board[i][j])
                else:
                    return False
        for k in range(9):
            visited = set()
            for i in range(k % 3 * 3, k % 3 * 3 + 3):
                for j in range(k // 3 * 3, k // 3 * 3 + 3):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] not in visited:
                        visited.add(board[i][j])
                    else:
                        return False
        return True

        
        
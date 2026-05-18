class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(idx, i, j):
            if idx == len(word) - 1:
                return board[i][j] == word[idx]
            if board[i][j] != word[idx]:
                return False
            visited.add((i, j))
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if (x, y) not in visited and 0 <= x < len(board) and 0 <= y < len(board[0]) and dfs(idx + 1, x, y):
                    return True
            visited.remove((i, j))
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(0, i, j):
                    return True
        return False
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1) and board[i][j] == 'O':
                    queue.append((i, j))
        while queue:
            i, j = queue.popleft()
            if board[i][j] == 'T': continue
            board[i][j] = 'T'
            if i+1 < len(board) and board[i+1][j] == 'O':
                queue.append((i+1, j))
            if i-1 >= 0 and board[i-1][j] == 'O':
                queue.append((i-1, j))
            if j+1 < len(board[0]) and board[i][j+1] == 'O':
                queue.append((i, j+1))
            if j-1 >= 0 and board[i][j-1] == 'O':
                queue.append((i, j-1))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
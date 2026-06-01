class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                islands += 1
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    grid[x][y] = '0'
                    for dx, dy in d:
                        if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]) and grid[x+dx][y+dy] == '1':
                            q.append((x+dx, y+dy))
        return islands

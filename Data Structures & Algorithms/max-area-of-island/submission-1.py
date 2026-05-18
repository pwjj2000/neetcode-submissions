class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                area = 0
                queue = [(i, j)]
                while queue:
                    x, y = queue.pop(0)
                    if grid[x][y] == 0:
                        continue
                    grid[x][y] = 0
                    area += 1
                    if x-1 >= 0 and grid[x-1][y] == 1:
                        queue.append((x-1, y))
                    if x+1 < m and grid[x+1][y] == 1:
                        queue.append((x+1, y))
                    if y-1 >= 0 and grid[x][y-1] == 1:
                        queue.append((x, y-1))
                    if y+1 < n and grid[x][y+1] == 1:
                        queue.append((x, y+1))
                if area > max_area:
                    max_area = area
                
        return max_area
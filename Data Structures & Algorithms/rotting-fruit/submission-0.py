class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue, visited = deque(), set()
        max_steps, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        while queue:
            i, j, steps = queue.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            grid[i][j] = 2
            if steps > max_steps:
                max_steps = steps
            if i+1<m and grid[i+1][j] == 1:
                queue.append((i+1, j, steps + 1))
            if i-1>=0 and grid[i-1][j] == 1:
                queue.append((i-1, j, steps + 1))
            if j+1<n and grid[i][j+1] == 1:
                queue.append((i, j+1, steps + 1))
            if j-1>=0 and grid[i][j-1] == 1:
                queue.append((i, j-1, steps + 1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return max_steps
        
        
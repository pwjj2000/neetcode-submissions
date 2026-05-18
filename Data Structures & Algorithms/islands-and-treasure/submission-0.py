class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue, visited = deque(), set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        def is_land(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if grid[i][j] <= 0:
                return False
            return True
        while queue:
            i, j, steps = queue.popleft()
            if (i, j) in visited:
                continue
            grid[i][j] = steps
            visited.add((i, j))
            if is_land(i + 1, j):
                queue.append((i+1, j, steps + 1))
            if is_land(i - 1, j):
                queue.append((i-1, j, steps + 1))
            if is_land(i, j+1):
                queue.append((i, j+1, steps + 1))
            if is_land(i, j-1):
                queue.append((i, j-1, steps + 1))
        



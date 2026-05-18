class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        heapq.heapify(heap)
        visited, n = set(), len(grid) - 1
        while heap:
            level, i, j = heapq.heappop(heap)
            if i == n == j:
                return level
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if i + 1 <= n:
                heapq.heappush(heap, (max(level, grid[i+1][j]), i+1, j))
            if i - 1 >= 0:
                heapq.heappush(heap, (max(level, grid[i-1][j]), i-1, j))
            if j + 1 <= n:
                heapq.heappush(heap, (max(level, grid[i][j+1]), i, j+1))
            if j - 1 >= 0:
                heapq.heappush(heap, (max(level, grid[i][j-1]), i, j-1))
            
        
            
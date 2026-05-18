class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp, self.longest = {}, 0
        def dfs(i, j, prev):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] <= prev:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            lip = 1
            for node in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                lip = max(lip, 1 + dfs(node[0], node[1], matrix[i][j]))
            dp[(i, j)] = lip
            self.longest = max(self.longest, lip)
            return lip
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j, -1)
        return self.longest
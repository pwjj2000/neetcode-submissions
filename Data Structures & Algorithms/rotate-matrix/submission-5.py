class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        half = len(matrix) // 2
        for i in range(half):
            for j in range(i, n - 1 - i):
                v1, v2, v3, v4 = matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i]
                matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i], matrix[i][j] = v1, v2, v3, v4
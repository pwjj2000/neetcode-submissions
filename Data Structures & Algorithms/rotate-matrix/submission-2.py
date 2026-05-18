class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        times = len(matrix) // 2
        for i in range(times):
            for j in range(i, n - 1 - i):
                a, b, c, d = matrix[i][j], matrix[j][n-1-i], matrix[m-1-i][n-1-j], matrix[m-1-j][i]
                matrix[i][j] = d
                matrix[j][n-1-i] = a
                matrix[m-1-i][n-1-j] = b
                matrix[m-1-j][i] = c
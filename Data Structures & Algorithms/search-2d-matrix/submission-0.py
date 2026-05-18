class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, m * n - 1
        while i <= j:
            row, col = i // n, i % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                i = row * n + col + 1
            elif matrix[row][col] > target:
                j = row * n + col - 1
        return False


        
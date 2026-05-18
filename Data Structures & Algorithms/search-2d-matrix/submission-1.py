class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n
        while left < right:
            mid = (left + right) // 2
            r, c = mid // n, mid % n
            if matrix[r][c] < target:
                left = mid + 1
            elif matrix[r][c] > target:
                right = mid
            else:
                return True
        return False
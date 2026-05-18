class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lmost, rmost, umost, dmost = 0, len(matrix[0]) - 1, 1, len(matrix) - 1
        total = len(matrix) * len(matrix[0])
        i, j, d, answer = 0, 0, 0, []
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for _ in range(total):
            answer.append(matrix[i][j])
            if d == 0 and j == rmost:
                d = (d + 1) % 4
                rmost -= 1
            elif d == 1 and i == dmost:
                d = (d + 1) % 4
                dmost -= 1
            elif d == 2 and j == lmost:
                d = (d + 1) % 4
                lmost += 1
            elif d == 3 and i == umost:
                d = (d + 1) % 4
                umost += 1
            i += direction[d][0]
            j += direction[d][1]
        return answer
class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0] * (n + 1)
        for i in range(n + 1):
            c, j = 0, i
            while j > 0:
                c += (j & 1)
                j >>= 1
            answer[i] = c
        return answer 

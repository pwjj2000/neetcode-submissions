class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        for _ in range(32):
            answer += (n & 1)
            n >>= 1
            answer <<= 1
        return answer >> 1
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            num, total = n, 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            n = total
        return True
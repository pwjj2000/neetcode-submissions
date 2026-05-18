class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                prev_i, _ = stack.pop()
                res[prev_i] = i - prev_i
            stack.append((i, t))
        return res
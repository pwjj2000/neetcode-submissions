class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                idx, t = stack.pop()
                temperatures[idx] = i - idx
            stack.append((i, temperatures[i]))
        for i, _ in stack:
            temperatures[i] = 0
        return temperatures
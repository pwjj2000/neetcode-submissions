class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for p, s in pairs:
            t_remain = float(target - p) / s
            if not stack or t_remain > stack[-1]:
                stack.append(t_remain)
        return len(stack) 
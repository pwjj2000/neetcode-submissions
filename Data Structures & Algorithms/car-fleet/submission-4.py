class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_time = [(position[i], (target-position[i])/speed[i]) for i in range(len(speed))]
        pos_time.sort(key=lambda x: x[1])
        pos_time.sort(key=lambda x: x[0], reverse=True)
        stack = []
        for p, t in pos_time:
            if not stack or t > stack[-1][1]:   
                stack.append((p, t))
        return len(stack)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start_idx = i
            while stack and h < stack[-1][1]:
                prev_i, prev_h = stack.pop()
                maxArea = max(maxArea, prev_h * (i - prev_i))
                start_idx = prev_i
            stack.append((start_idx, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
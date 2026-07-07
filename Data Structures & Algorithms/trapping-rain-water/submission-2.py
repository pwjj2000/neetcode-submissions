class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        for i in range(len(height) - 1):
            prefix[i+1] = max(prefix[i], height[i])
            suffix[len(height)-2-i] = max(suffix[len(height)-1-i], height[len(height)-1-i])
        total = 0
        for i in range(len(height)):
            total += max(0, min(prefix[i], suffix[i]) - height[i])
        return total
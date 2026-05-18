class Solution:
    def trap(self, height: List[int]) -> int:
        prefix, suffix = [0] * len(height), [0] * len(height)
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i - 1], height[i - 1])
            suffix[len(height) - 1 - i] = max(suffix[len(height) - i], height[len(height) - i])
        maxAmount = 0
        for i in range(len(height)):
            maxAmount += max(0, min(prefix[i], suffix[i]) - height[i])
        return maxAmount

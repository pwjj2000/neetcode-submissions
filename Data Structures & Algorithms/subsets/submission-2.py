class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s = []
        def dfs(i, arr):
            if i == len(nums):
                s.append(arr.copy())
                return
            dfs(i+1, arr)
            arr.append(nums[i])
            dfs(i+1, arr)
            arr.pop()
        dfs(0, [])
        return s

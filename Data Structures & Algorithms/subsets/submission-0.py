class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets_length = 2**len(nums)
        subsets = [[] for _ in range(subsets_length)]
        for i in range(subsets_length):
            for j in range(len(nums)):
                if i & 2**j > 0:
                    subsets[i].append(nums[j])
        return subsets
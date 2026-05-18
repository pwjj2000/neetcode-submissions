class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, curr = [], []
        nums.sort()
        def ksum(k, l, target):
            r = len(nums) - 1
            if k == 2:
                while l < r:
                    if nums[l] + nums[r] < target:
                        l += 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append(curr + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l-1] == nums[l]:
                            l += 1
                        while r > l and nums[r+1] == nums[r]:
                            r -= 1
            else:
                for i in range(l, len(nums) - k + 1):
                    if i > l and nums[i] == nums[i - 1]:
                        continue
                    curr.append(nums[i])
                    ksum(k - 1, i + 1, target - nums[i])
                    curr.pop()
        ksum(4, 0, target)
        return res
                


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        count = 0
        idx, curr = 0, nums[0]
        skip = 0
        while count < len(nums):
            idx = (idx + k) % len(nums)
            temp = nums[idx]
            nums[idx] = curr
            curr = temp
            count += 1
            if idx == skip and count < len(nums):
                idx += 1
                skip += 1
                curr = nums[idx]
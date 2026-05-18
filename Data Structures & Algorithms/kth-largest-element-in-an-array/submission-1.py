class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        rank = len(nums) - k
        def quickselect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]
            if p < rank:
                quickselect(p + 1, r)
            elif p > rank:
                quickselect(l, p - 1)
            else:
                return 
        quickselect(0, len(nums) - 1)
        return nums[len(nums) - k]

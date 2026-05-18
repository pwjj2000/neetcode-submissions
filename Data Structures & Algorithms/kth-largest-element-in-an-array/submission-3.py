class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        rank = len(nums) - k
        def quickselect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p == rank:
                return
            elif p > rank:
                quickselect(l, r - 1)
            else:
                quickselect(l + 1, r)
        quickselect(0, len(nums) - 1)
        return nums[rank]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (r - l) // 2 + l
            if target > nums[r]:
                if nums[mid] <= nums[r]:
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid
            else:
                if nums[mid] > nums[r]:
                    l = mid + 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid

        return l if nums[l] == target else -1
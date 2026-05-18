class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] < nums[right]:
                if target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[mid] < nums[right]:
                if target <= nums[mid]:
                    right = mid
                elif target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[left]:
                    left = mid + 1
                else:
                    right = mid

        if nums[left] == target:
            return left
        else:
            return -1
        
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = {}
        mini, maxi = float('inf'), float('-inf') 
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if num < mini:
                mini = num
            if num > maxi:
                maxi = num
        idx = 0
        for i in range(mini, maxi + 1):
            while count.get(i, 0):
                nums[idx] = i
                idx += 1
                count[i] -= 1
        return nums
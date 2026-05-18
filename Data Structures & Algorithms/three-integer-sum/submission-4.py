class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            complement = {}
            target = -nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] not in complement:
                    complement[target - nums[j]] = 0
                elif complement[nums[j]] == 0:
                    triplets.append([nums[i], target - nums[j], nums[j]])
                    complement[nums[j]] = 1
                else:
                    continue
        return triplets
                    

        
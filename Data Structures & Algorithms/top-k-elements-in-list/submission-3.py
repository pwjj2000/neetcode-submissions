class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        freq = {}
        for key, val in count.items():
            if val not in freq:
                freq[val] = []
            freq[val].append(key)
        ans = []
        for i in reversed(range(1, len(nums) + 1)):
            if k == 0:
                break
            while i in freq and freq[i]:
                ans.append(freq[i].pop())
                k -= 1
        return ans


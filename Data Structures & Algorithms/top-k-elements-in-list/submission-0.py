class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq.keys():
                freq[num] = 1
            else:
                freq[num] += 1
        return [sorted(freq.items(), key=lambda item: item[1], reverse=True)[i][0] for i in range(k)]
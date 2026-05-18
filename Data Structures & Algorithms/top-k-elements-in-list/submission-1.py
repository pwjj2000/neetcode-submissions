class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        sorted_freq = sorted(freq.items(), reverse=True, key=lambda x: x[1])
        return [f[0] for f in sorted_freq][:k]
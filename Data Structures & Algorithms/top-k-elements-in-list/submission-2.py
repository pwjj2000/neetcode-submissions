class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        freq = [[] for _ in range(len(nums) + 1)]
        for c in count:
            freq[count[c]].append(c)
        res, idx = [], len(nums)
        while k > 0:
            if freq[idx]:
                res.append(freq[idx].pop())
                k -= 1
            else:
                idx -= 1
        return res
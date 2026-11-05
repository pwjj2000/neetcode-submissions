class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        freq = defaultdict(list)
        for key, v in list(count.items()):
            freq[v].append(key)
        ans = []
        for i in reversed(range(len(nums)+1)):
            if len(freq[i]) <= k:
                ans.extend(freq[i])
                k -= len(freq[i])
            else:
                ans.extend(freq[i][:k])
                break
        return ans

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            smallest = heapq.heappop(stones)
            smallest2 = heapq.heappop(stones)
            res = smallest - smallest2
            if res != 0:
                heapq.heappush(stones, res)
        return -stones[0] if stones else 0

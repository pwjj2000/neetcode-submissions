class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for p in points:
            dist = -(p[0]*p[0] + p[1]*p[1])
            heapq.heappush(heap, (dist, p))
            if len(heap) > k:
                heapq.heappop(heap)
        return [t[1] for t in heap]
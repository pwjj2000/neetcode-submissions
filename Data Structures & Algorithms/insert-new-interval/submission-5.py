class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if newInterval[0] > intervals[mid][0]:
                l = mid + 1
            else:
                r = mid - 1
        intervals.insert(l, newInterval)
        res = []
        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
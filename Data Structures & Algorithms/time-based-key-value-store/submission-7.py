class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.timemap[key] or timestamp < self.timemap[key][0][1]:
            return ""
        l, r = 0, len(self.timemap[key]) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if self.timemap[key][mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        return self.timemap[key][l-1][0]

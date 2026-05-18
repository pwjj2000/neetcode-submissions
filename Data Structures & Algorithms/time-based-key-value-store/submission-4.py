class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]
        left, right = 0, len(values)
        while left < right:
            mid  = (left + right) // 2
            if timestamp < values[mid][0]:
                right = mid
            else:
                left = mid + 1
        if left > 0:
            return values[left - 1][1]
        else:
            return ""


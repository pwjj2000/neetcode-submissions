class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        curr, diff, c, ans = 0, float('inf'), deque(), None
        for i in range(len(arr)):
            if i < k:
                curr += abs(arr[i] - x)
                c.append(arr[i])
                if i == k - 1:
                    ans = c.copy()
                    diff = curr
            else:
                curr += abs(arr[i] - x) - abs(arr[i-k] - x)
                c.popleft()
                c.append(arr[i])
                if curr < diff:
                    diff = curr
                    ans = c.copy()
        return list(ans)

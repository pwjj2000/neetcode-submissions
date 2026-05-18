class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            prereq[c].append(p)
        visited, disregard = set(), set()
        res = []
        def dfs(c):
            if c in visited:
                return False
            if c in disregard:
                return True
            visited.add(c)
            for p in prereq[c]:
                if not dfs(p):
                    return False
            visited.remove(c)
            res.append(c)
            disregard.add(c)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
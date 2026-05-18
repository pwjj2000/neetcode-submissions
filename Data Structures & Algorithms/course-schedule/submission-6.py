class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            prereq[c].append(p)
        visited = set()
        def dfs(c):
            if c in visited:
                return False
            if not prereq[c]:
                return True
            visited.add(c)
            for p in prereq[c]:
                if not dfs(p):
                    return False
            visited.remove(c)
            prereq[c] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
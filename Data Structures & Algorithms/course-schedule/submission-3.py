class Node:
    def __init__(self, val: int):
        self.course = val
        self.children = []
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nextCourse = {}
        for c in range(numCourses):
            nextCourse[c] = []
        for p in prerequisites:
            nextCourse[p[1]].append(p[0])
        queue = deque([(c, c, n) for c in nextCourse.keys() for n in nextCourse[c]])
        while queue:
            origin, src, dest = queue.popleft()
            if dest == origin:
                return False
            queue.extend([(origin, dest, c) for c in nextCourse[dest]])
        return True
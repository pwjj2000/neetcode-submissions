class Node:
    def __init__(self, val: int):
        self.course = val
        self.children = []
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = [Node(i) for i in range(numCourses)]
        for a, b in prerequisites:
            nodes[b].children.append(nodes[a])
        for node in nodes:
            visited = set()
            queue = deque([(None, node)])
            while queue:
                prereq, n = queue.popleft()
                if (prereq, n) in visited:
                    return False
                visited.add((prereq, n))
                for c in n.children:
                    queue.append((n,c))
        return True
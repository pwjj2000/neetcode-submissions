class Node:
    def __init__(self, val: int):
        self.course = val
        self.children = []
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = [Node(i) for i in range(numCourses)]
        for a, b in prerequisites:
            nodes[b].children.append(nodes[a])
        visited_node = set()
        for node in nodes:
            if node in visited_node:
                continue
            visited_edge = set()
            queue = deque([(None, node)])
            while queue:
                prereq, n = queue.popleft()
                if (prereq, n) in visited_edge:
                    return False
                visited_node.add(n)
                visited_edge.add((prereq, n))
                for c in n.children:
                    queue.append((n,c))
        return True
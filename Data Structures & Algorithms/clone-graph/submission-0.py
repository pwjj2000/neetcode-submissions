"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        queue, clone = [node], {}
        visited = set()
        while queue:
            n = queue.pop(0)
            if n in visited:
                continue
            visited.add(n)
            if n not in clone:
                clone[n] = Node(n.val)
            for neighbor in n.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                clone[n].neighbors.append(clone[neighbor])
                queue.append(neighbor)
        return clone[node]
            

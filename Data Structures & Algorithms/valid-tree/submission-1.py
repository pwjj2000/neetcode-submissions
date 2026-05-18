class Solution:

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        class Node:
            def __init__(self, val: int):
                self.val = val
                self.neighbors = []
        visited = [False] * n
        nodes = [Node(i) for i in range(n)]
        for edge in edges:
            if edge[0] == edge[1]: return False
            nodes[edge[0]].neighbors.append(edge[1])
            nodes[edge[1]].neighbors.append(edge[0])
        queue = [0]
        while queue:
            i = queue.pop(0)
            if visited[i]:
                return False
            visited[i] = True
            for neighbor in nodes[i].neighbors:
                if not visited[neighbor]:
                    queue.append(neighbor)
        for v in visited:
            if not v:
                return False
        return True

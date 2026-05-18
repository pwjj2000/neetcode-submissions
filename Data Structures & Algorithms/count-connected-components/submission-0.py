class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class Node:
            def __init__(self, val: int):
                self.val = val
                self.neighbors = []
        visited = [False] * n
        nodes = [Node(i) for i in range(n)]
        for edge in edges:
            if edge[0] != edge[1]: 
                nodes[edge[0]].neighbors.append(edge[1])
                nodes[edge[1]].neighbors.append(edge[0])
        count = 0
        for i in range(len(visited)):
            if not visited[i]:
                count += 1
                queue = [i]
                while queue:
                    node = queue.pop(0)
                    if visited[node]:
                        continue
                    visited[node] = True
                    for n in nodes[node].neighbors:
                        if not visited[n]:
                            queue.append(n)
        return count
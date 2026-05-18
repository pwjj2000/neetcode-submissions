class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacQ, atlQ = deque(), deque()
        for i in range(len(heights)):
            pacQ.append((i, 0))
            atlQ.append((i, len(heights[0]) - 1))
        for j in range(len(heights[0])):
            pacQ.append((0, j))
            atlQ.append((len(heights) - 1, j))
        pacVisited, atlVisited = set(), set()
        while pacQ:
            i, j = pacQ.popleft()
            if (i, j) in pacVisited:
                continue
            pacVisited.add((i, j))
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if (x, y) not in pacVisited and 0 <= x < len(heights) and 0 <= y < len(heights[0]) and heights[i][j] <= heights[x][y]:
                    pacQ.append((x, y))
        while atlQ:
            i, j = atlQ.popleft()
            if (i, j) in atlVisited:
                continue
            atlVisited.add((i, j))
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if (x, y) not in atlVisited and 0 <= x < len(heights) and 0 <= y < len(heights[0]) and heights[i][j] <= heights[x][y]:
                    atlQ.append((x, y))
        return list(pacVisited & atlVisited)
        
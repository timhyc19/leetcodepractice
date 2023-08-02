import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set() # (r, c)
        maxArea = 0

        def bfs(r, c):
            total = 1
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                islandR, islandC = q.popleft()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in directions:
                    r, c = islandR + dr, islandC + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visited):
                        visited.add((r, c))
                        q.append((r, c))
                        total += 1
            
            return total

        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)
        
        return maxArea
    
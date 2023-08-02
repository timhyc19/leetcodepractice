class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set() # (r, c)

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols)
                    and (r, c) not in visited and grid[r][c] == "1"):
                        visited.add((r, c))
                        q.append((r, c))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    # check all the neighbours that are 1's, and mark as visited
                    bfs(r, c)

                    # increment islands
                    islands += 1
        
        return islands
    
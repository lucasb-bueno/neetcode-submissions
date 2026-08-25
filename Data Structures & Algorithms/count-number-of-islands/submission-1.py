class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        visited = set()
        islands = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()
                
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    xr = row + dr
                    xc = col + dc
                    if (xr in range(rows) and xc in range(cols) and grid[xr][xc] == "1" and (xr, xc) not in visited):
                        queue.append((xr, xc))
                        visited.add((xr, xc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
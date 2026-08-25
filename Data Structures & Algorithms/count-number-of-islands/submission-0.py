class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    drow = dr + row
                    dcol = dc + col
                    if (drow in range(rows) and
                     dcol in range(cols) and
                      grid[drow][dcol] == "1"  and
                       (drow, dcol) not in visited):
                        q.append((drow, dcol))
                        visited.add((drow, dcol))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands
        
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(grid, visited, r, c):
            if (min(r, c) < 0 or ROWS == r or COLS == c or (r, c) in visited or grid[r][c] == 1):
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            visited.add((r, c))

            count = 0

            count += dfs(grid, visited, r + 1, c)
            count += dfs(grid, visited, r - 1, c)
            count += dfs(grid, visited, r, c + 1)
            count += dfs(grid, visited, r, c - 1)

            visited.remove((r, c))

            return count

        return dfs(grid, set(), 0, 0)



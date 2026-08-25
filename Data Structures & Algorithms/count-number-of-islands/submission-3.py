class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        notes:
        - return num of connected 1's in the grid (graph)
        - the edges are water (0's)
        - defines island:
            - 0 <= pos < ROWS, COLS (out of bounds)
            - visiting all nodes always (BFS)
            - check if node is visited
            - check if node is == "1"
        
        
        - iterate through each pos in grid and run bsf to check if has an island
            - in order to run bfs, we check if item is != 0 and item is not visited
            - run BFS
            - increase island number   

        """

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        island = 0
        visited = set()
        
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] != "0":
                        print((nr, nc))
                        q.append((nr, nc))
                        visited.add((nr, nc))



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != "0" and (r, c) not in visited:
                    island += 1
                    bfs(r, c)

        return island   
            




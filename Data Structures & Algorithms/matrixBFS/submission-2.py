class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        queue = deque()

        queue.append((0, 0))
        visited.add((0, 0))

        length = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if ROWS - 1 == r and COLS - 1 == c:
                    return length
                
                neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in neighbors:
                    row = dr + r
                    col = dc + c
                    if (min(row, col) < 0 or row == ROWS or col == COLS or (row, col) in visited or grid[row][col] == 1):
                        continue
                    queue.append((row, col))
                    visited.add((row, col))
            length += 1
        return -1



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
                
                neighbors = [[1, 0], [0, 1], [0, -1], [-1, 0]]
                for dr, dc in neighbors:
                    if (min(dr + r, dc + c) < 0 or r + dr == ROWS or dc + c == COLS or (dr + r, dc + c) in visited or grid[dr + r][dc + c] == 1):
                        continue
                    queue.append((dr + r, dc + c))
                    visited.add(((dr + r, dc + c)))
            length += 1
        return -1
                    




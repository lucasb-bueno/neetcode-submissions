class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            L, R = 0, len(matrix[r]) - 1

            while L <= R:
                middle = (L + R) // 2
                if matrix[r][middle] < target:
                    L = middle + 1
                elif matrix[r][middle] > target:
                    R = middle - 1
                else:
                    return True
        return False

                

        
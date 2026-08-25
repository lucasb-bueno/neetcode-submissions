class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Cols = len(matrix), len(matrix[0])

        L, R = 0, Rows - 1
        while L <= R:
            middle = (L + R) // 2
            if target > matrix[middle][-1]:
                L = middle + 1
            elif target < matrix[middle][0]:
                R = middle - 1
            else:
                break
            
        if not (L <= R):
            return False
        rightRow = (L + R) // 2
        l, r = 0, Cols - 1
        while l <= r:
            middle = (l + r) // 2
            if target > matrix[rightRow][middle]:
                l = middle + 1
            elif target < matrix[rightRow][middle]:
                r = middle - 1
            else:
                return True
        return False 

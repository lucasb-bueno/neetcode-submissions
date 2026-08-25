class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            total = 0
            rowSum = []
            for c in range(cols):
                total += matrix[r][c]
                rowSum.append(total)
            self.prefix.append(rowSum)
        print(self.prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2 + 1):
            if col1 > 0:
                res += self.prefix[row][col2] - self.prefix[row][col1 - 1]
            else:
                res += self.prefix[row][col2]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
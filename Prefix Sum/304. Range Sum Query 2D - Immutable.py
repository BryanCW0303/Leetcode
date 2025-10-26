from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n+1) for _ in range(m+1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + x
        self.s = s

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.s[row2+1][col2+1] - self.s[row2+1][col1] - self.s[row1][col2+1] + self.s[row1][col1]
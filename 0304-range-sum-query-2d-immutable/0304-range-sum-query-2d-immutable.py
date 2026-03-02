class NumMatrix:
    @staticmethod
    def prefix_sum(matrix):
        row  = len(matrix)
        column = len(matrix[0])
        prefix = [[0]*(column + 1) for i in range(row + 1)]

        for r, row in enumerate(matrix):
            for c in range(len(row)):
                prefix[r+1][c+1] = matrix[r][c] + prefix[r][c+1] + prefix[r+1][c] - prefix[r][c]
        return prefix

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = NumMatrix.prefix_sum(matrix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p = self.prefix
        sum_2d = p[row2+1][col2+1] - p[row1][col2+1] - p[row2+1][col1] + p[row1][col1]
        return sum_2d
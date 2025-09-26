class NumMatrix:
    def prefixSum(self):
        matrix = self.matrix
        row  = self.row
        column = self.column

        prefix = [[0]*(column + 1) for i in range(row + 1)]
        for r, row in enumerate(matrix):
            for e in range(len(row)):
                prefix[r+1][e+1] = matrix[r][e] + prefix[r][e+1] + prefix[r+1][e] - prefix[r][e]
        return prefix
    def print(self,matrix:List[List[int]]):
        for row in matrix:
            r = ""
            for e in row:
                r += f"{e} "
            print(r)
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.row  = len(matrix)
        self.column = len(matrix[0])
        self.prefix = self.prefixSum()
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        prefix = self.prefix
        sum = prefix[row2+1][col2+1] - prefix[row1][col2+1] - prefix[row2+1][col1] + prefix[row1][col1]
        return sum
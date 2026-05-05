class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_list = set()
        column_list = set()
        row = len(matrix)
        column = len(matrix[0])
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0:
                    row_list.add(i)
                    column_list.add(j)
        for i in range(row):
            for j in range(column):
                if i in row_list or j in column_list:
                    matrix[i][j] = 0
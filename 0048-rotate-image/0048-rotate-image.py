class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows):
            for j in range(i, columns):
                matrix[i][j], matrix[j][i] = matrix[j][i] ,matrix[i][j]
        for i in range(rows):
            for j in range(columns//2):
                rev = columns - j - 1
                matrix[i][j], matrix[i][rev] = matrix[i][rev] ,matrix[i][j]
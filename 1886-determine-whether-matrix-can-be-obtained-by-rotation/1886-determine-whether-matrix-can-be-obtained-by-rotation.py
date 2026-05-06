class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
            rows = len(matrix)
            columns = len(matrix[0])
            for i in range(rows):
                for j in range(i, columns):
                    matrix[i][j], matrix[j][i] = matrix[j][i] ,matrix[i][j]
            for i in range(rows):
                for j in range(columns//2):
                    rev = columns - j - 1
                    matrix[i][j], matrix[i][rev] = matrix[i][rev] ,matrix[i][j]
        def isEqual(mat1,mat2):
            rows = len(mat1)
            columns = len(mat1[0])
            for i in range(rows):
                for j in range(columns):
                    if mat1[i][j] != mat2[i][j]:
                        return False
            return True
        for _ in range(4):
            if isEqual(mat,target):
                return True
            rotate(mat)
        return False
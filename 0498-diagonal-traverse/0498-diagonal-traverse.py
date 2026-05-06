class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        reverse = True
        total = rows + cols - 1
        result = []
        diagonals = [[] for i in range(total)]
        for i in range(rows):
            for j in range(cols):
                diagonals[i+j].append(mat[i][j])
        for d in diagonals:
            if reverse:
                d.reverse()
            result.extend(d)
            reverse = not reverse
        return result
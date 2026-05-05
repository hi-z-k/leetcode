class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        row = len(matrix)
        column = len(matrix[0])
        total = row * column
        top = 0
        bottom = row - 1
        left = 0
        right = column - 1
        while top <= bottom and left <= right:
            for j in range(left,right+1):
                spiral.append(matrix[top][j])
            top += 1
            for i in range(top,bottom+1):
                spiral.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for j in range(right,left-1,-1):
                    spiral.append(matrix[bottom][j])
                bottom -= 1
            if left <= right:
                for i in range(bottom,top-1,-1):
                    spiral.append(matrix[i][left])
                left += 1
        return spiral

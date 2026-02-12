class Solution:
    @staticmethod
    def smooth(matrix, r, c):
        total = 0
        count = 0
        row = len(matrix)
        col = len(matrix[0])
        for i in range(r-1,r+2):
            for j in range(c-1,c+2):
                if 0 <= i < row and 0 <= j < col:
                    total += matrix[i][j]
                    count += 1
        return total // count
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        smooth = Solution.smooth
        output = [[element for element in row] for row in img]
        
        for i, row in enumerate(img):
            for j,element in enumerate(row):
                output[i][j] = smooth(img,i,j)

        return output
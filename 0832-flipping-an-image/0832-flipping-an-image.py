class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows = len(image)
        columns = len(image[0])
        for i in range(rows):
            for j in range(columns):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
            image[i].reverse()
        return image
        
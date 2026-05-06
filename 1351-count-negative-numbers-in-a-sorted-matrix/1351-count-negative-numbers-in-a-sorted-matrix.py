class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols-1,-1,-1):
                num = grid[i][j]
                if num > -1:
                    break
                count += 1
        return count
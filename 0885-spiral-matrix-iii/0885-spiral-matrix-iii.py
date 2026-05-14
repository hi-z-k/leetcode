class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = [[rStart, cStart]]
        r, c = rStart, cStart
        scale = 1
        d = 0
        
        while len(result) < rows * cols:
            for _ in range(2):
                dr, dc = directions[d]
                for _ in range(scale):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                    if len(result) == rows * cols:
                        return result
                d = (d + 1) % 4
            scale += 1
            
        return result
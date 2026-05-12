class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        while left <= right:
            middle = left + (right-left)//2
            element = matrix[middle][0]
            if element == target:
                return True
            elif element > target:
                right = middle - 1
            else:
                left = middle + 1
        row = matrix[right]
        l = 0
        r = len(row) - 1
        while l <= r:
            m = l + (r-l)//2
            element = row[m]
            if element == target:
                return True
            elif element > target:
                r = m - 1
            else:
                l = m + 1
        return False
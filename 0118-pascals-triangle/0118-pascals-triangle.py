class Solution:
    @staticmethod
    def pascalRow(nums):
        result = [1]
        for i in range(1,len(nums)):
            result.append(nums[i-1]+nums[i])
        result.append(1)
        return result
    def generate(self, numRows: int) -> List[List[int]]:
        pascalRow = Solution.pascalRow
        result = [[1],[1,1]]
        recent = result[-1]
        if numRows == 1:
            return [[1]]
        for i in range(2,numRows):
            result.append(pascalRow(result[-1]))
        return result
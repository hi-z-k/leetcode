class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        rangeList = set()
        for row in ranges:
            for element in range(row[0],row[1]+1):
                rangeList.add(element)
        for num in range(left,right+1):
            if num not in rangeList:
                return False
        return True
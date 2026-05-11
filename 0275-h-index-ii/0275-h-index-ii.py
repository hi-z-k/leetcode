class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)-1

        while left <= right:
            middle = left + (right-left)//2
            cited = citations[middle]
            count = len(citations)-middle
            if cited == count:
                return cited
            elif cited < count:
                left = middle + 1
            else:
                right = middle - 1

        return len(citations)-left
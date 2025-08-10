class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0 
        j = len(nums)-1
        sortedList = []
        while (i<=j):
            numI = nums[i]**2
            numJ = nums[j]**2
            if numI < numJ:
                sortedList.append(numJ)
                j -= 1
            else:
                sortedList.append(numI)
                i += 1
        return sortedList[::-1]
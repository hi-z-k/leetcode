class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        i = 0 
        j = len(nums)-1
        k = j
        sortedList = [0]*(k+1)
        while (i<=j):
            numI = nums[i]**2
            numJ = nums[j]**2
            if numI < numJ:
                sortedList[k] = numJ
                j -= 1
            else:
                sortedList[k] = numI
                i += 1
            k-=1
        return sortedList
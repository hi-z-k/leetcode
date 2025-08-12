class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        uniqueCount = 1
        while (j < len(nums)):
            numI = nums[i]
            numJ = nums[j]
            j += 1
            if numI == numJ:
                continue
            nums[uniqueCount] = nums[j-1]
            uniqueCount += 1
            i = j-1
        return uniqueCount
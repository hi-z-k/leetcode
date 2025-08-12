class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        totalCount = len(nums)
        uniqueIdx = [0]
        while (j < totalCount):
            numI = nums[i]
            numJ = nums[j]
            j += 1
            if numI == numJ:
                continue
            uniqueIdx.append(j-1)
            i = j-1
        uniqueCount = len(uniqueIdx)
        for i in range(totalCount):
            if i < uniqueCount:
                nums[i] = nums[uniqueIdx[i]]
            else:
                nums[i] = -1

        return uniqueCount
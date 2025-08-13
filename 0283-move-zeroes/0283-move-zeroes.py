class Solution:
    def moveZeroes(self, nums: list[int]):
        i = 0
        j = 1
        while (j < len(nums)):
            numI = nums[i]
            numJ = nums[j]
            if numJ == 0 and numI == 0:
                j += 1
            elif numI == 0 and numJ != 0:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                i+=1
                j+=1
        return nums
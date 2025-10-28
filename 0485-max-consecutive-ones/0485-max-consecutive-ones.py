class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length = 0
        maxLength = 0
        i = 0
        for j in range(len(nums)):
            if nums[j]:
                length += 1
                maxLength = max(maxLength,length)
            else:
                length = 0
        return maxLength
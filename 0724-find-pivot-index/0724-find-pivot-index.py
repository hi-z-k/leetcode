class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0
        for i,num in enumerate(nums):
            rightSum -= num
            if rightSum == leftSum:
                return i
            leftSum += num
        return -1

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = 0
        rightSum = sum(nums)
        sumDiff = []
        for num in nums:
            rightSum -= num
            sumDiff.append(abs(leftSum - rightSum))
            leftSum += num
        return sumDiff
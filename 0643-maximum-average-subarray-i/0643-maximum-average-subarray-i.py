class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        j = k
        currentSum = sum(nums[:k])
        maxSum = currentSum
        while (j < len(nums)):
            currentSum -= nums[j-k]
            currentSum += nums[j]
            maxSum = max(maxSum,currentSum)
            j += 1
        return maxSum/k
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumOfthefirstK = sum(nums[:k])
        j = k
        currentSum = sumOfthefirstK
        maxSum = sumOfthefirstK
        while (j < len(nums)):
            currentSum -= nums[j-k]
            currentSum += nums[j]
            if(currentSum > maxSum):
                maxSum = currentSum
            j += 1
        return maxSum/k
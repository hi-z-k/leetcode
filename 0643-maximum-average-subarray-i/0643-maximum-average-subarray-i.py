class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumOfthefirstK = sum(nums[:k])
        idx = 0
        currentSum = sumOfthefirstK
        maxSum = sumOfthefirstK
        while (idx < len(nums) - k):
            currentSum -= nums[idx]
            currentSum += nums[idx+k]
            if(currentSum > maxSum):
                maxSum = currentSum
            idx += 1
        return maxSum/k
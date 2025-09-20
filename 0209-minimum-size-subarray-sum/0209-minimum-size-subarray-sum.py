class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currentLength = 0
        length = float("inf")
        i = 0
        currentSum = 0
        for j in range(len(nums)):
            currentSum += nums[j]
            currentLength += 1
            while currentSum >= target:
                length = min(length,currentLength)
                currentSum -= nums[i]
                i += 1
                currentLength -= 1
        if (length > len(nums)): return 0
        return int(length)
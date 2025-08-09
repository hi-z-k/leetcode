class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumOfthefirstK = 0
        for i in range(k):
            sumOfthefirstK += nums[i]
        idx = 0
        sumList = []
        while (idx < len(nums) - k):
            sumList.append(sumOfthefirstK)
            sumOfthefirstK -= nums[idx]
            sumOfthefirstK += nums[idx+k]
            idx += 1
        sumList.append(sumOfthefirstK)
        return max(sumList)/k
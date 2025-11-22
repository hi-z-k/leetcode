class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        prefixSum = []
        for num in nums:
            sum += num
            prefixSum.append(sum)
        return prefixSum
        
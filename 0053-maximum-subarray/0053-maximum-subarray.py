class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        maximum_sum = float("-inf")
        for num in nums:
            curr_sum = max(num, curr_sum + num)
            maximum_sum = max(maximum_sum,curr_sum)
        return maximum_sum
        
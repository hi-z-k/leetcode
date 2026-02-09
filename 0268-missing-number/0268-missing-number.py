class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr_sum = sum(nums)
        n = len(nums)
        ideal_sum = int(n * (n+1)/2)
        return ideal_sum - curr_sum
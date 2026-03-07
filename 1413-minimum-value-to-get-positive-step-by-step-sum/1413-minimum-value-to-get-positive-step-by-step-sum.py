class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [0]
        min_val = 0
        for num in nums:
            curr_prefix = num+prefix[-1]
            min_val = min(min_val, curr_prefix)
            prefix.append(curr_prefix)
        return abs(min_val) + 1
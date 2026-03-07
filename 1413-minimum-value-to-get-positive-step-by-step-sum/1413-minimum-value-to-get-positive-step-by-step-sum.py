class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(num+prefix[-1])
        min_val = min(prefix)
        return abs(min_val) + 1
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_diff = 0
        if len(nums) < 2:
            return 0
        for i in range(len(nums)-1):
            left,right = nums[i:i+2]
            max_diff = max(max_diff, right-left)
        return max_diff
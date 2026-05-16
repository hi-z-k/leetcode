class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        next_val = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= next_val:
                next_val = nums[i]
            else:
                parts = (nums[i] + next_val - 1) // next_val
                count += parts - 1
                next_val = nums[i] // parts
        
        return count
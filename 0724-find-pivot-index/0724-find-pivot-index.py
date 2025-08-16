class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumRight = sum(nums) - nums[0]
        sumLeft = 0
        i = 0
        while(i < len(nums)):
            if sumLeft == sumRight:
                return i
            sumLeft += nums[i]
            i += 1
            if(i < len(nums)): sumRight -= nums[i]
        return -1
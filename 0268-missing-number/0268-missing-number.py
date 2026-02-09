class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxNum = len(nums)
        nums = set(nums)
        for num in range(maxNum+1):
            if num not in nums:
                return num
        return -1
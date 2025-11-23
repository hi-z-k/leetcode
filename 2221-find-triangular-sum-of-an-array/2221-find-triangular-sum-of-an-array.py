class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        length = len(nums)
        while(length > 1):
            newNums = []
            for i in range(1,length):
                newNums.append((nums[i-1]+nums[i])%10)
            nums = newNums
            length = len(nums)
        return nums[0]
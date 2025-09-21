class NumArray:
    def __init__(self, nums:List[int]):
        self.nums = nums
        self.prefix = self.prefixSum(nums)
    def prefixSum(self, nums):
        prefix = []
        prefix.append(0)
        for i in range(1,len(nums)+1):
            prefix.append(prefix[i-1] + nums[i-1])
        return prefix
    def sumRange(self,left,right):
        prefix = self.prefix
        nums = self.nums
        return prefix[right + 1] - prefix[left]

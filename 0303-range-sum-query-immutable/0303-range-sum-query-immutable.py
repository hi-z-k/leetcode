class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_calc()
    def prefix_calc(self):
        nums = self.nums
        self.prefix = [0]
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        prefix = self.prefix
        return prefix[right+1] - prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
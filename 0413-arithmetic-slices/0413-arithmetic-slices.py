class Solution:
    @staticmethod
    def counter(num):
        num -= 2
        return int(num *(num+1)/2)
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        counter = Solution.counter
        if len(nums) == 1:
            return 0
        diff = nums[1]-nums[0]
        count = 0
        length = 2
        i = 0
        for j in range(2,len(nums)):
            if nums[j]-nums[j-1] == diff:
                length += 1
                continue

            diff = nums[j]-nums[j-1]
            count += counter(length)
            length = 2
        count += counter(length)
        return count
        
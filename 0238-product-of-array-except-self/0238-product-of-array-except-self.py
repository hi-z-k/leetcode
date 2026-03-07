class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        output = [0]*len(nums)
        product = reduce(lambda x, y: x * y, (x for x in nums if x != 0), 1)
        if zero_count > 1:
            pass
        elif zero_count == 1:
            i = nums.index(0)
            output[i] = product
        else:
            for i,num in enumerate(nums):
                output[i] = product//num
        return output
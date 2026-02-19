class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(d) for d in nums]
        nums.sort(key=lambda x: x*10, reverse = True)
        return "".join(nums)
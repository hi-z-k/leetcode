class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set(nums)
        return len(nums) != len(uniqueNums)
        
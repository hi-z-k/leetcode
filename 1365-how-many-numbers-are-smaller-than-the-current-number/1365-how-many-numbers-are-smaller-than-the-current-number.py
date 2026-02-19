class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        loc={}
        for i, num in enumerate(sorted(nums)):
            if num not in loc:
                loc[num] = i
        output = [loc[num] for num in nums]
        return output
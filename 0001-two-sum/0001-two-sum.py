class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        requiredBefore = {}
        for i, num in enumerate(nums):
            requireNum = target-num
            if requireNum in requiredBefore:
                return [requiredBefore[requireNum],i]
            else:
                requiredBefore[num] = i
        return []
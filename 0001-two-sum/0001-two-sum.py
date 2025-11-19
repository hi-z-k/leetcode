class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for i,n in enumerate(nums):
            needed = target - n
            if n in targets:
                return [targets[n],i]
            targets[needed] = i
        return []

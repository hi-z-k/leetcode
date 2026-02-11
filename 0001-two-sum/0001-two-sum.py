class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map = {}
        for j,num in enumerate(nums):
            needed = target - num
            if num in target_map:
                i = target_map[num]
                return [i,j]
            target_map[needed] = j
            print(needed,j)
        return -1
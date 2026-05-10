class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def backtrack(i):
            if  len(path) > 1:
                result.append(path[:])
            collected = set()
            for j in range(i, len(nums)):
                num = nums[j]
                if path and num < path[-1] or num in collected:
                    continue
                collected.add(num)
                path.append(num)
                backtrack(j+1)
                path.pop()
        backtrack(0)
        return result
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        path_already = set()
        def backtrack():
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for num in nums:
                if num in path_already:
                    continue
                path.append(num)
                path_already.add(num)
                backtrack()
                path.pop()
                path_already.remove(num)
        backtrack()
        return ans
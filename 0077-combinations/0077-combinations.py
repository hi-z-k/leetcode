class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def combination(i):
            if len(path) == k:
                ans.append(path[:])
                return 
            for j in range(i, n+1):
                path.append(j)
                combination(j+1)
                path.pop()
        combination(1)
        return ans
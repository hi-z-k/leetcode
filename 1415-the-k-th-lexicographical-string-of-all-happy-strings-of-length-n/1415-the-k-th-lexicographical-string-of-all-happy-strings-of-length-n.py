class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ["a","b","c"]
        result = []
        path = []
        def backtrack():
            if len(path) == n:
                result.append("".join(path))
                return
            for l in letters:
                if path and path[-1] == l:
                    continue
                path.append(l)
                backtrack()
                path.pop()
        backtrack()
        try:
            return result[k-1]
        except Exception: 
            return ""
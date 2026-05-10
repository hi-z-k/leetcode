class Solution:
    def smallestNumber(self, pattern: str) -> str:
        digits = [1,2,3,4,5,6,7,8,9]
        path = []
        visited = set()
        def valid(start,end,rule):
            if rule == "I":
                return start < end
            else:
                return start > end
            
        def backtrack(i):
            if len(path) == len(pattern)+1:
                num = "".join([str(n) for n in path])
                return num
            for d in digits:
                m = len(path) - 1
                if (path and not valid(path[-1],d,pattern[m])) or d in visited:
                    continue
                path.append(d)
                visited.add(d)
                result = backtrack(i+1)
                if result: 
                    return result
                path.pop()
                visited.remove(d)
        return backtrack(0)

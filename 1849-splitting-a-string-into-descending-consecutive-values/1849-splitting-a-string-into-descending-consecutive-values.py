class Solution:
    def splitString(self, s: str) -> bool:
        result = []
        path = []
        def backtrack(i):
            if i == len(s):
                if len(path) > 1:
                    return True
                return False
            for j in range(i+1,len(s)+1):
                num = int(s[i:j])
                if path and num >= path[-1]:
                    break
                elif (path and path[-1] - num == 1) or not path:
                    path.append(num)
                    if backtrack(j):
                        return True
                    path.pop()
                    
        if backtrack(0):
            return True
        return False

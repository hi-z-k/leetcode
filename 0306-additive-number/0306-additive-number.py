class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        path = []
        def backtrack(i):
            if i == len(num):
                if len(path) > 2:
                    return True
                else:
                    return False
            for j in range(i+1, len(num)+1):
                n = int(num[i: j])
                if num[i] == "0" and j > i+1:
                    break
                if len(path) > 1:
                    total = path[-1]+path[-2]
                    if total > n:
                        continue
                    elif total < n:
                        break
                path.append(n)
                if backtrack(j): 
                    return True
                path.pop()
            return False
        return backtrack(0)

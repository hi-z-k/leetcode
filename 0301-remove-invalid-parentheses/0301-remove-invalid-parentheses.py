class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(string):
            stack = []
            for char in string:
                if char == '(':
                    stack.append('(')
                elif char == ')':
                    if not stack:
                        return False
                    stack.pop()
            return not stack

        result = set()
        path = []
        count = 0
        minCount = len(s)

        def backtrack(i):
            nonlocal count, minCount, result
            
            if count > minCount:
                return

            if i == len(s):
                par = "".join(path)
                if isValid(par):
                    if count < minCount:
                        minCount = count
                        result = {par}
                    elif count == minCount:
                        result.add(par)
                return 
            
            curr = s[i]
            
            if curr not in "()":
                path.append(curr)
                backtrack(i + 1)
                path.pop()
            else:
                path.append(curr)
                backtrack(i + 1)
                path.pop()

                count += 1
                backtrack(i + 1)
                count -= 1

        backtrack(0)
        return list(result)
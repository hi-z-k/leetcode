class Solution:
    @staticmethod
    def resultingStr(string:str) -> str:
        stack = []
        for l in string:
            if l != "#":
                stack.append(l)
                continue
            if stack:
                stack.pop()
        return ("").join(stack)
    def backspaceCompare(self, s: str, t: str) -> bool:
        finalStr = Solution.resultingStr
        return finalStr(s) == finalStr(t)
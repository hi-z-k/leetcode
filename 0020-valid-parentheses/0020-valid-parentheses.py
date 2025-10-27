class Solution:
    @staticmethod
    def complemet(closing):
        match = {
            ")":"(",
            "]" : "[",
            "}" : "{"
        }
        return match[closing]
    @staticmethod
    def isOpeningBracket(bracket):
        return bracket in {"(","{","["}
    def isValid(self, s: str) -> bool:
        stack = []
        complemet = Solution.complemet
        isOpeningBracket = Solution.isOpeningBracket
        for b in s:
            if isOpeningBracket(b):
                stack.append(b)
                continue
            try:
                top = stack[-1]
            except IndexError:
                return False
            if complemet(b) != top:
                return False
            else:
                stack.pop()
        return not len(stack)
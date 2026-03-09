class Solution:
    def removeStars(self, s: str) -> str:
        characters = list(s)
        stack = []
        for ch in characters:
            if ch == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
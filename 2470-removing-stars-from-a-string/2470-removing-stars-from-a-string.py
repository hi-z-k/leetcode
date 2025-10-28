class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for letter in s:
            if letter != "*":
                stack.append(letter)
                continue
            if stack:
                stack.pop()
        return ("").join(stack)
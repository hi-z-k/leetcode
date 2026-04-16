class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = 0
        counter = 0
        for i,p in enumerate(s):
            if p == "(":
                stack += 1
            else:
                stack -= 1
                if s[i-1] == "(":
                    counter += 2 ** stack

        return counter
        
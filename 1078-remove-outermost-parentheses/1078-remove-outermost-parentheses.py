class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opening = []
        start = 0
        marked = set()
        for i,p in enumerate(s):
            if p == "(":
                opening.append(p)
            elif opening:
                opening.pop()
            if not opening and i:
                marked.add(start)
                marked.add(i)
                start = i + 1
        output = []
        for i,p in enumerate(s):
            if i not in marked:
                output.append(p)
        return ("").join(output)
        
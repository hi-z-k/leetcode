class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        #   you set the start when the ( stack and ) stack are empty
        #   when the sizes of the two stack becomes equal(if not empty), record the locations in the hash
        # go through the string once more and recreate the answer
        opening = []
        closing = []
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
        
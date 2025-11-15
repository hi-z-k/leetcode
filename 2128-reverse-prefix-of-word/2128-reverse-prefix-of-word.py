class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        for i,l in enumerate(word):
            stack.append(l)
            if l == ch:
                stack.reverse()
                stack.extend(list(word[i+1:]))
                return ("").join(stack)
        return word
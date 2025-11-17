class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for ch in s:
            try:
                num = int(ch)
                if stack:
                    stack.pop()
            except Exception:
                stack.append(ch)
        return ("").join(stack)
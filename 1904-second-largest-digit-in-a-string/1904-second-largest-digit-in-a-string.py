class Solution:
    def secondHighest(self, s: str) -> int:
        maxNum = -1
        secondNum = -1
        for l in s:
            if not l.isalpha():
                num = int(l)
                maxNum = max(maxNum, num)
        for l in s:
            if not l.isalpha():
                num = int(l)
                if num == maxNum:
                    continue
                secondNum = max(secondNum, num)
        return secondNum
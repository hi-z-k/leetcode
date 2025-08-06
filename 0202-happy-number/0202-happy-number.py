class Solution:
    def happy(self, n:int):
        sum = 0
        for digit in str(n):
            sum += int(digit)**2
        return sum

    def isHappy(self, n: int) -> bool:
        alreadyFound = {}
        while (n != 1):
            if (n not in alreadyFound):
                alreadyFound[n] = 1
                n = self.happy(n)
            else:
                return False
        return True
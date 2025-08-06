class Solution:
    def happy(self, n:int):
        sum = 0
        for digit in str(n):
            sum += int(digit)**2
        return sum

    def isHappy(self, n: int) -> bool:
        alreadyFound = set()
        while (n != 1):
            if (n not in alreadyFound):
                alreadyFound.add(n)
                n = self.happy(n)
            else:
                return False
        return True
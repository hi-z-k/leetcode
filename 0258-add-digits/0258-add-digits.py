class Solution:
    def sumDigits(self, num: int) -> int:
        sum = 0
        for digit in str(num):
            sum += int(digit)
        return sum
    def addDigits(self, num: int) -> int:
        if(num % 10 == num):
            return num
        return self.addDigits(self.sumDigits(num))
        
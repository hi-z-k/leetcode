class Solution:
    @staticmethod
    def getDigit(num:int)->List[int]:
        nums = [int(n) for n in list(str(num))]
        digits = [0]*(4-len(nums))
        digits.extend(nums)
        return digits

    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        digitOf = Solution.getDigit
        digit1 = digitOf(num1)
        digit2 = digitOf(num2)
        digit3 = digitOf(num3)
        output = []
        for i in range(len(digit1)):
            a,b,c = digit1[i], digit2[i], digit3[i]
            digit = min(a,b,c)
            output.append(str(digit))
        return int(('').join(output))
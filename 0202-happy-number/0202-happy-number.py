class Solution:
    @staticmethod
    def calculate(num):
        result = 0
        for digit in list(str(num)):
            result += int(digit) ** 2
        return result
    
    def isHappy(self, n: int) -> bool:
        calc = Solution.calculate
        results = set()
        while True:
            n = calc(n)
            if n in results:
                return False
            elif n == 1:
                break
            else:
                results.add(n)
        return True
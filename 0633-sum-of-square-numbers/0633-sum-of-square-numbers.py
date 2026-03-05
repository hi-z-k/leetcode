class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = (c ** 0.5)//1
        while (a <= b):
            result = a ** 2 + b ** 2
            if result == c:
                return True
            elif result < c:
                a += 1
            else:
                b -= 1
        return False
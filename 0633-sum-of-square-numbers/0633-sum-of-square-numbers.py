class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(c ** 0.5)
        while(i <= j):
            sum = i ** 2 + j ** 2
            if sum == c: 
                return True
            elif c < sum:
                j -= 1
            else:
                i += 1
        return False
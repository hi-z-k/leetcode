class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(c ** 0.5)
        while(i <= j):
            print(i,j)
            sum = i ** 2 + j ** 2
            diff = c - sum
            if not diff: 
                return True
            elif diff < 0:
                j -= 1
            else:
                i += 1
        print(i,j)
        return False
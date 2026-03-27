class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n < 0:
                n *= -1
                x = 1/x
            elif n == 0:
                return 1.0

            half_next = power(x,n//2)
            output = 1
            if n % 2 != 0:
                output *= x
            output *= (half_next * half_next)
            return output
        return power(x,n)
  
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        intdiv = n//4
        div = n/4
        if (n == 1):
            return True
        if (intdiv != div or n==0):
            return False
        
        else:
            return self.isPowerOfFour(intdiv)
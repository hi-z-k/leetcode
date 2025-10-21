class Solution:
    def fib(self, n: int) -> int:
        fibMin1 = 1
        fibMin2 = 0
        fibN = 1
        if not n: return n
        for i in range(1,n):
            fibN = fibMin1 + fibMin2
            fibMin2 = fibMin1
            fibMin1 = fibN
        return fibN
        
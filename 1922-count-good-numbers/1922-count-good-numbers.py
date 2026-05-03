class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # even position => even(5 options)
        # odd position => prime(4 options)
        # 5 => e,o,e,o,e => odd => evens index = half + 1
        # even => even index = half
        M = 10**9 + 7
        prime_count = n//2
        even_count = n - prime_count
        return (pow(5, even_count, M) * pow(4, prime_count, M)) % M

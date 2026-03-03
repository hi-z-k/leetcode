class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)//3 
        i = 1
        total = 0
        for _ in range(n):
            total += piles[i]
            i += 2
        return total
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def isPile(curr_pile):
            p = 0
            for c in candies:
                p += c//curr_pile
            return k <= p
        total = sum(candies)
        if total < k:
            return 0

        result = 0
        left = 1
        right = total//k
        while left <= right:
            middle = (left+right)//2
            if isPile(middle):
                result = middle
                left = middle + 1
            else:
                right = middle - 1
        return result
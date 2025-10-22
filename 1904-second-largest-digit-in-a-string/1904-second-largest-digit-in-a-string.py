class Solution:
    def secondHighest(self, s: str) -> int:
        maxN = float("-inf")
        secondMax = float("-inf")
        for l in s:
            if not l.isalpha():
                num = int(l)
                if num > maxN:
                    secondMax = maxN
                    maxN = num
                elif num > secondMax and num < maxN:
                    secondMax = num
        if secondMax == float("-inf"): return -1
        return int(secondMax)
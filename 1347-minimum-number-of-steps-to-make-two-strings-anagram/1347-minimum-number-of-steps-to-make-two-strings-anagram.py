class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countS = Counter(s)
        countT = Counter(t)
        diff = countT - countS
        total = 0
        for n,m in diff.items():
            total += m
        return total
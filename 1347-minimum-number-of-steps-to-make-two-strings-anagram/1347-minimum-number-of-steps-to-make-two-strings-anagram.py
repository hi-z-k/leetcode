class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countS = Counter(s)
        countT = Counter(t)
        diff = countT - countS
        total = 0
        for m in diff.values():
            total += m
        return total
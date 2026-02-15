class Solution:
    def minSteps(self, s: str, t: str) -> int:
        diff = (Counter(t)-Counter(s)).values()
        return sum(diff)
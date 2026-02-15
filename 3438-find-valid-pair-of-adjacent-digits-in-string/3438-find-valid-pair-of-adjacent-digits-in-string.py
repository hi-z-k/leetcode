class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter([int(n) for n in s])
        valid = set()
        for n in count:
            if n == count[n]:
                valid.add(str(n))
        for i in range(len(s)-1):
            first = s[i]
            second = s[i+1]
            if first == second:
                continue
            if first in valid and second in valid:
                return s[i:i+2]
        return ""
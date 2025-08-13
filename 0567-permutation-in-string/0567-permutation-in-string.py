from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        checkStr = Counter(s1)
        i = 0
        j = window

        while (j <= len(s2)):
            segmentStr = Counter(s2[i:j])
            i += 1
            j += 1
            if checkStr == segmentStr:
                return True
        return False
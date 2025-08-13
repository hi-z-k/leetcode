class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        checkStr = Counter(s1)
        segmentStr = Counter(s2[:window])
        i = 0
        j = window

        while (j <= len(s2)):
            if checkStr == segmentStr:
                return True
            segmentStr[s2[i]] -= 1
            if j < len(s2): segmentStr[s2[j]] = segmentStr.get(s2[j], 0) + 1
            i += 1
            j += 1
        return False
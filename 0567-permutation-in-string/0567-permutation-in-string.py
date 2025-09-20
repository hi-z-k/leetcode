class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        targetCount = Counter(s1)
        windowCount = Counter(s2[:window])
        i = 0
        j = window

        while (j <= len(s2)):
            if targetCount == windowCount:
                return True
            if j == len(s2): break
            windowCount[s2[i]] -= 1
            i += 1
            windowCount[s2[j]] += 1
            j += 1
        return False
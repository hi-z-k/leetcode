class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        subStrings = []
        maxIdx = {}
        for i, l in enumerate(s):
            maxIdx[l] = i
        currMax = maxIdx[s[0]]
        currStart = 0
        for i in range(len(s)):
            letter = s[i]
            lastIdx = maxIdx[letter]
            if i > currMax:
                length = currMax - currStart + 1
                currStart = i
                subStrings.append(length)
                currMax = lastIdx
            else:
                currMax = max(currMax, lastIdx)
        length = currMax - currStart + 1
        subStrings.append(length)
        return subStrings
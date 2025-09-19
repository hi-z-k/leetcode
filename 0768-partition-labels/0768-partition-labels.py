class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        subStrings = []
        maximumSubStr = {}
        for index, letter in enumerate(s):
            maximumSubStr[letter] = index
        currMax = maximumSubStr[s[0]]
        currStart = 0
        for i in range(len(s)):
            letter = s[i]
            lastIdx = maximumSubStr[letter]
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
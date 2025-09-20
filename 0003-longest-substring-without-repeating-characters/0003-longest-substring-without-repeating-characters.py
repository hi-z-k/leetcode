class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setWindow = set()
        i = 0
        currentLength = 0
        length = 0
        for j in range(len(s)):
            while s[j] in setWindow:
                setWindow.remove(s[i])
                currentLength -= 1
                i += 1
            setWindow.add(s[j])
            currentLength += 1
            length = max(length, currentLength)
        return length
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)
        target = haystack[:k]
        for i in range(len(haystack)-k+1):
            target = haystack[i:i+k]
            if target == needle:
                return i

        return -1
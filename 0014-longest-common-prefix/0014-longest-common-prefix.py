from collections import Counter
class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        prefix = strs[0]
        for s in strs:
            while not s.startswith(prefix) and prefix:
                prefix = prefix[:-1]
        return prefix
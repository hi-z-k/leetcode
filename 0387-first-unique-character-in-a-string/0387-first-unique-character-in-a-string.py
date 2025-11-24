from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i,letter in enumerate(s):
            if count[letter] == 1:
                return i
        return -1
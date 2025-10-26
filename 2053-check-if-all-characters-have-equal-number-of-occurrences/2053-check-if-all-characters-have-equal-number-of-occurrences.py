from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        checker = count[s[0]]
        for letter in count:
            if count[letter] != checker:
                return False
        return True
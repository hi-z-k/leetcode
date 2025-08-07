from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dictS = Counter(s)
        for letter in t:
            if letter not in dictS or dictS[letter] == 0:
                return letter
            dictS[letter] -= 1
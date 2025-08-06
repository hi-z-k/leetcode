class Solution:
    def count(self,lst):
            occurrence = {}
            for i, data in enumerate(lst):
                if data in occurrence:
                    occurrence[data].append(i)
                else:
                    occurrence[data] = [i]
            return occurrence

    def firstUniqChar(self, s: str) -> int:
        freqCount = self.count(s)
        for letter in freqCount:
            indexList = freqCount[letter]
            if len(indexList) == 1:
                return indexList[0]
        return -1
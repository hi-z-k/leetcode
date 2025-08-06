class Solution:
    def count(self,lst):
            occurrence = {}
            for i, data in enumerate(lst):
                if data not in occurrence:
                    occurrence[data] = i
                else:
                    occurrence[data] = -1   
            return occurrence

    def firstUniqChar(self, s: str) -> int:
        freqCount = self.count(s)
        for letter in freqCount:
            index = freqCount[letter]
            if index != -1:
                return index
        return -1
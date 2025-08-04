class Solution:
    def frequencyDict(self,lst):
        occurenece = {}
        for data in lst:
            occurenece[data] = occurenece.get(data,0) + 1
        return occurenece

    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s): return False
        
        freqDictT = self.frequencyDict(t)
        for char in s:
            if (char in freqDictT) and (freqDictT[char] > 0):
                freqDictT[char] -= 1
                continue
            return False
        return True
            
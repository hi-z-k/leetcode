class Solution:
    def count(self,lst):
        occurenece = {}
        for data in lst:
            occurenece[data] = occurenece.get(data,0) + 1
        return occurenece

    def compare(self,dict1, dict2):
        keyDelete = []
        for element in list(dict1.keys()):
            if dict2.get(element,0):
                dict1[element] = min(dict1[element],dict2[element])
            else:
                del dict1[element]
        return dict1

    def strOf(self,dict):
        strOut = ""
        for c in dict:
            strOut += c*dict[c]
        return list(strOut)


    def commonChars(self, words: list[str]) -> list[str]:
        if len(words)== 0: return []
        superSet = self.count(words[0])
        for word in words[1:]:
            wordFreq = self.count(word)
            superSet = self.compare(superSet,wordFreq)
        return self.strOf(superSet)
    



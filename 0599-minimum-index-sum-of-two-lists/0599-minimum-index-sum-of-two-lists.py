class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idxList1 = {}
        commonWords = {}
        for i,word in enumerate(list1):
            idxList1[word] = i
            
        for j,word in enumerate(list2):
            if word in idxList1:
                commonWords[word] = j + idxList1[word]
        
        firstKey = next(iter(commonWords))
        minVal = commonWords[firstKey]
        minSet = {firstKey}
        for word in commonWords:
            wordVal = commonWords[word]
            if wordVal < minVal:
                minSet = {word}
                minVal = wordVal
            elif wordVal == minVal:
                minSet.add(word)

        return list(minSet)
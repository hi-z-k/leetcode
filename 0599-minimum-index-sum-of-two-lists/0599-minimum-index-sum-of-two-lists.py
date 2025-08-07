class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idxList1 = {}
        for i,word in enumerate(list1):
            idxList1[word] = i

        minVal = len(list1)+len(list2)
        minSet = set() 
        for j,word in enumerate(list2):
            if word in idxList1:
                wordVal = j + idxList1[word]
                if wordVal < minVal:
                    minSet = {word}
                    minVal = wordVal
                elif wordVal == minVal:
                    minSet.add(word)
        return list(minSet)
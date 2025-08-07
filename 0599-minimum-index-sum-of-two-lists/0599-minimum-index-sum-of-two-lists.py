class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idxList1 = {word: i for i,word in enumerate(list1)}

        minVal = len(list1)+len(list2)
        minList = []
        for j,word in enumerate(list2):
            if word in idxList1:
                wordVal = j + idxList1[word]
                if wordVal < minVal:
                    minList = [word]
                    minVal = wordVal
                elif wordVal == minVal:
                    minList.append(word)
        return minList
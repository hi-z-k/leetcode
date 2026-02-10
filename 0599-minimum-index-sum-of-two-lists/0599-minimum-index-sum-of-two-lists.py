class Solution:
    @staticmethod
    def hashmap(list1):
        output = {}
        for i,e in enumerate(list1):
            output[e] = i
        return output
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = Solution.hashmap
        map1 = hashmap(list1)
        map2 = hashmap(list2)
        common = set(list1) & set(list2)
        commonMap = {}
        for string in common:
            commonMap[string] = map1[string] + map2[string]
        minIdx = min(commonMap.values())
        output = []
        for string in commonMap:
            if commonMap[string] == minIdx:
                output.append(string)
        return output

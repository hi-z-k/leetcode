from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        lenCount = [[] for _ in range(len(nums)+1)]
        for c in count:
            freq = count[c]
            lenCount[freq].append(c)
            j = len(lenCount[freq])-1   
            while j>0 and lenCount[freq][j] > lenCount[freq][j-1]:
                lenCount[freq][j], lenCount[freq][j-1] = lenCount[freq][j-1], lenCount[freq][j]
                j -= 1
        output = []
        for i in range(len(lenCount)):
            for num in lenCount[i]:
                output.extend([num]*i)
        return output
        
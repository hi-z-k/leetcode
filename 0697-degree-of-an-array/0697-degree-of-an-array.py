class Solution:
    def numOccurence(self, nums: List[int]) -> Dict[int, Dict[str, int]]: 
        numsHash = {}
        for index,num in enumerate(nums):
            if num not in numsHash:
                val = {}
                val["first"] = index
                val["last"] = index
                val["count"] = 1
                numsHash[num] = val
            else:
                numsHash[num]["count"] += 1
                numsHash[num]["last"] = index
        return numsHash
    def findShortestSubArray(self, nums: List[int]) -> int:
        numsDict = self.numOccurence(nums)
        maxFrequency = max([data["count"] for data in numsDict.values()])
        possibleLength = [data["last"]-data["first"]+1 for data in numsDict.values() if data["count"]== maxFrequency]
        return min(possibleLength)
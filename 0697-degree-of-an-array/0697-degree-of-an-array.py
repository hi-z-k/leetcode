class Solution:
    def numOccurence(self, nums: List[int]) -> Dict[int, Dict[str, int]]: 
        numsHash = {}
        for index,num in enumerate(nums):
            if num not in numsHash:
                numsHash[num] = {"first": index, "last": index, "count": 1}
            else:
                numsHash[num]["count"] += 1
                numsHash[num]["last"] = index
        return numsHash
    def length(self,start, end):
        return end - start + 1
    def findShortestSubArray(self, nums: List[int]) -> int:
        numsDict = self.numOccurence(nums)
        maxFrequency = max((data["count"] for data in numsDict.values()))
        leastLength = min((self.length(data["first"], data["last"]) for data in numsDict.values() if data["count"]== maxFrequency))
        return leastLength
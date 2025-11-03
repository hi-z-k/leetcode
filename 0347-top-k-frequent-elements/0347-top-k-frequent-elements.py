class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        lenCount = [[] for _ in range(len(nums)+1)]
        for c in count:
            freq = count[c]
            lenCount[freq].append(c)
        topK = []
        for i in range(len(lenCount)-1,-1,-1):
            nums = lenCount[i]
            if not nums:
                continue
            for n in nums:
                if len(topK) == k:
                    return topK
                topK.append(n)
        return topK
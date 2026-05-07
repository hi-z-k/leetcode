class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        val = 0
        for i,c in enumerate(citations):
            if c >= i+1:
                val = i + 1
            else:
                break
        return val

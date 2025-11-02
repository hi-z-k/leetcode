class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        lookup = {}
        last = len(heights) - 1
        for i, height in enumerate(heights):
            lookup[height] = names[i]
        for i in range(last, -1,-1):
            for j in range(last,last-i-1,-1):
                if heights[j] > heights[j-1]:
                    heights[j], heights[j-1] = heights[j-1], heights[j]
        for i, height in enumerate(heights):
            heights[i] = lookup[height]
        return heights

        
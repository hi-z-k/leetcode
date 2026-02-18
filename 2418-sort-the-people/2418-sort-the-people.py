class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height = {height: name for name, height in zip(names, heights)}
        for i in range(len(heights)):
            min_idx = max(range(i, len(heights)), key=lambda idx: heights[idx])
            heights[i], heights[min_idx] = heights[min_idx],heights[i]
        for i in range(len(heights)):
            name = height[heights[i]]
            names[i] = name
        return names
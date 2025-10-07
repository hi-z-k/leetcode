class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxHeight = 0
        currentGain = 0
        for change in gain:
            currentGain += change
            maxHeight = max(maxHeight,currentGain)
        return maxHeight
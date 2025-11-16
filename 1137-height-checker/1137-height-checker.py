class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        freq = [0]*101
        expected = [0]*len(heights)
        for h in heights:
            freq[h] += 1
        for i in range(1,len(freq)):
            freq[i] += freq[i-1]
        for i in range(len(heights)-1,-1,-1):
            element = heights[i]
            freqNum = freq[element]
            if freqNum:
                expected[freqNum-1] = element
                freq[element] -= 1
        count = 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                count += 1
        return count
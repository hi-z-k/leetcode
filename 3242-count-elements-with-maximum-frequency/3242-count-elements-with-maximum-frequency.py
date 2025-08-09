class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqNums = Counter(nums)
        maxFrequency = max(freqNums.values())
        maxFreqEltCount = 0
        for frequency in freqNums.values():
            if frequency == maxFrequency:
                maxFreqEltCount += frequency
        return maxFreqEltCount
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqNums = Counter(nums)
        maxFrequency = max(freqNums.values())
        maxFreqEltCount = 0
        for num in freqNums:
            if freqNums[num] == maxFrequency:
                maxFreqEltCount += freqNums[num]
        return maxFreqEltCount
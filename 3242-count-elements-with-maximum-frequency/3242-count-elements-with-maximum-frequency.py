class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqNums = Counter(nums)
        maxFrequency = max(freqNums.values())
        maxFreqEltCount = 0
        for num in nums:
            if freqNums[num] == maxFrequency:
                maxFreqEltCount += 1
        return maxFreqEltCount
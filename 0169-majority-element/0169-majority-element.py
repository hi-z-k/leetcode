from collections import Counter
from math import floor
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqNums = Counter(nums)
        majorityCount = floor(len(nums)/2)
        for num in freqNums:
            if freqNums[num] > majorityCount:
                return num
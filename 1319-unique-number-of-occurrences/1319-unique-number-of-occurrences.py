from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency = Counter(arr).values()
        freqSet = set(frequency)
        return len(frequency) == len(freqSet)

from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = Counter(nums)
        freq = [-1]*(len(nums)+1)
        for n in count:
            if n % 2 != 0:
                continue
            idx = count[n]
            if freq[idx] == -1:
                freq[idx] = n
            else:
                freq[idx] = min(freq[idx], n)
        for i in range(len(freq)-1,-1,-1):
            if freq[i] == -1:
                continue
            return freq[i]
        return -1
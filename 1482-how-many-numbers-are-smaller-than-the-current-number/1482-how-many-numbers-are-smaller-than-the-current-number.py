class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0]*101
        for n in nums:
            freq[n] += 1
        for i in range(1,101):
            freq[i] += freq[i-1]
        lessThan = []
        for n in nums:
            count = 0
            if n:
                count = freq[n-1]
            lessThan.append(count)
           
        return lessThan
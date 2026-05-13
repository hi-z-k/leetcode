class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        countPrefix = [0]*(len(nums)+1)
        for l,r in requests:
            countPrefix[l] += 1
            countPrefix[r+1] -= 1
        for i in range(1,len(countPrefix)):
            countPrefix[i] += countPrefix[i-1]
        countPrefix.pop()

        countPrefix.sort()
        nums.sort()
        total = 0
        MOD = 10**9 + 7
        
        for count, num in zip(countPrefix, nums):
            total = (total + count * num) % MOD
            
        return total

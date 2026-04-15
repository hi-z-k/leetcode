class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxLength = 0
        length = 0
        zeroCount = 0
        i = 0
        for j in range(len(nums)):
            length += 1
            if not nums[j]:
                zeroCount += 1
            while zeroCount > 1:
                length -= 1
                if not nums[i]:
                    zeroCount -= 1
                i += 1       
            maxLength = max(maxLength,length-1)
        return maxLength
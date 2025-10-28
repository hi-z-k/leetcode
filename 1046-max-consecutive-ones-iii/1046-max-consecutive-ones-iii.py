class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        length = 0
        maxLength = 0
        zeroCount = 0
        for j in range(len(nums)):
            length += 1
            if not nums[j]:
                zeroCount += 1
            while zeroCount > k and i <= j:
                if not nums[i]:
                    zeroCount -= 1
                length -= 1
                i += 1
            maxLength = max(maxLength, length)
        return maxLength
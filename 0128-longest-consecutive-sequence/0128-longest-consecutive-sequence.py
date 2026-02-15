class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        check = set(nums)
        length = 1
        maxLength = 1
        for num in check:
            prev = num - 1
            nextN = num + 1
            if prev not in check:
                while nextN in check:
                    length += 1
                    nextN += 1
                maxLength = max(length,maxLength)
                length = 1
        return maxLength
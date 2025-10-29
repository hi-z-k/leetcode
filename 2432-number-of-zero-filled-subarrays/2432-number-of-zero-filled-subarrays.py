class Solution:
    @staticmethod
    def totalSubarray(length:int)->int:
        return int(length*(length+1)/2)
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        zeroCount = 0
        for n in nums:
            totalSubarray = Solution.totalSubarray
            if not n:
                zeroCount += 1
            else:
                total += totalSubarray(zeroCount)
                zeroCount = 0
        total += totalSubarray(zeroCount)
        return total
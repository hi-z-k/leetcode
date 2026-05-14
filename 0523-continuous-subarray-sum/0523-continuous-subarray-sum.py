class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        sumBefore = defaultdict(int)
        sumBefore[0] = -1
        for i,s in enumerate(nums):
            rem = s % k
            if rem in sumBefore:
                if i - sumBefore[rem] > 1:
                    return True
            else:
                sumBefore[rem] = i
        return False

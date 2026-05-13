class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        sumBefore = defaultdict(int)
        sumBefore[0] = 1
        count = 0
        for s in nums:
            rem = s % k
            if rem in sumBefore:
                count += sumBefore[rem]
            sumBefore[rem] += 1
        return count
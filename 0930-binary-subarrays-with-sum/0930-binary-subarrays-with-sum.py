class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(goal):
            i = 0
            total = 0
            subarrays = 0
            for j in range(len(nums)):
                total += nums[j]
                while total > goal and i <= j:
                    total -= nums[i]
                    i += 1
                subarrays += j - i + 1
            return subarrays
        return atMost(goal) - atMost(goal-1)
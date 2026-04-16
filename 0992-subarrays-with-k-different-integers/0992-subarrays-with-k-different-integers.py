class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarrayAtMostK(k: int) -> int:
            frequency = defaultdict(int)
            i = 0
            count = 0
            for j in range(len(nums)):
                frequency[nums[j]] += 1
                while len(frequency) > k and i < len(nums):
                    frequency[nums[i]] -= 1
                    if not frequency[nums[i]]:
                        del frequency[nums[i]]
                    i += 1
                count += j - i + 1
            return count
        return subarrayAtMostK(k) - subarrayAtMostK(k-1)

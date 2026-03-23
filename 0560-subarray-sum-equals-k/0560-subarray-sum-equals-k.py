class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq_map = defaultdict(int)
        freq_map[0] = 1
        total = 0
        count = 0
        for j in range(len(nums)):
            total += nums[j]
            needed = total - k
            if needed in freq_map:
                count += freq_map[needed]
            freq_map[total] += 1
        return count
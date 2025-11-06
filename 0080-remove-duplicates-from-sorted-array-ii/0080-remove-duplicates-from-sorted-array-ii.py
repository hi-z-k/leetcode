from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = Counter(nums)
        visited = set()
        i = 0
        for n in nums:
            if n not in visited:
                visited.add(n)
                length = min(count[n],2)
                for _ in range(length):
                    nums[i] = n
                    i += 1
        return i
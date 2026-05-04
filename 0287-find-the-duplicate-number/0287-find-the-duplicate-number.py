class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        for n,m in count.items():
            if m >= 2:
                return n
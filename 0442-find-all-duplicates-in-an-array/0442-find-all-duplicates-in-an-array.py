class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        repeated = []
        for n,m in count.items():
            if m > 1:
                repeated.append(n)
        return repeated
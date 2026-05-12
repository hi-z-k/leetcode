class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        duplicate = -1
        for num, freq in count.items():
            if freq == 2:
                duplicate = num
                break
        n = len(nums)
        total = (n * (n + 1))//2
        missing = total - sum(count.keys())
        return [duplicate, missing]
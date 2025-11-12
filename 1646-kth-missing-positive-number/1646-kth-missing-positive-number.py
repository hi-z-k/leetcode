class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        num = 0
        nums = set(arr)
        while (count < k):
            num += 1
            if num not in nums:
                count += 1
        return num
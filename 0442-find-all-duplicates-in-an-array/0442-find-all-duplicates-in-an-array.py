class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        previous_num = set()
        repeated = []
        for num in nums:
            if num in previous_num:
                repeated.append(num)
            previous_num.add(num)
        return repeated
        
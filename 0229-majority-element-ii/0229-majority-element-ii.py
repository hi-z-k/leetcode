class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        countNum = Counter(nums)
        minCount = int(len(nums)/3)
        majority = []
        for num, count in countNum.items():
            if count > minCount:
                majority.append(num)
        return majority

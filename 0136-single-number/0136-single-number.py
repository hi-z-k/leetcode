class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        element = set()
        for n in nums:
            if n not in element:
                element.add(n)
            else:
                element.remove(n)
        for unique in element:
            return unique
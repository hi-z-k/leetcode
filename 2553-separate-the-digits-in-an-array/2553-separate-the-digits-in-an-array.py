class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        digits = []
        for num in nums:
            digit = [int(d) for d in list(str(num))]
            digits.extend(digit)
        return digits
        
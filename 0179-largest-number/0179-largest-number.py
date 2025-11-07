class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numStr = [str(n) for n in nums]
        numStr.sort(key=lambda n: n*10, reverse=True)
        num = ("").join(numStr)
        try:
            return str(int(num))
        except Exception:
            return num
    
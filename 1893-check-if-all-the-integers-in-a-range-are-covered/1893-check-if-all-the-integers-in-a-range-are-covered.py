class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums = set()
        for start, end in ranges:
            nums.update(range(start,end+1))
        ints = set(range(left,right+1))
        return ints <= nums
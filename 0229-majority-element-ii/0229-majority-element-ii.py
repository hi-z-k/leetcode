from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        freq = int(len(nums)/3)
        output = []
        for n in count:
            if freq < count[n]:
                output.append(n)
        return output
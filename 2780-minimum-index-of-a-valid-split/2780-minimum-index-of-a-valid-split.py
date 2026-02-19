class Solution:
    @staticmethod
    def check(count,length): 
        return count * 2 > length
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums).most_common(1)[0]
        countL = 0
        dominant,countR = count
        for i,num in enumerate(nums):
            check = Solution.check
            if num == dominant:
                countR -= 1
                countL += 1
            lenL = i+1
            lenR = len(nums)-lenL
            if check(countL,lenL) and check(countR,lenR):
               return i
        return -1
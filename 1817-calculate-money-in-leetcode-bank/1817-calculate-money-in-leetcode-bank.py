class Solution:
    ONE_WEEK = 7
    @staticmethod
    def total(start:int,step:int)-> int:
        if(step < 0):
            raise ValueError("You can't have negative indexes")
        return step  * (2 * start + (step - 1))//2
    @staticmethod
    def weeklyTotal(weekNum)-> int:
        ONE_WEEK = Solution.ONE_WEEK
        return ONE_WEEK*(weekNum+4)
    
    def totalMoney(self, n: int) -> int:
        ONE_WEEK = Solution.ONE_WEEK
        weekly = Solution.weeklyTotal
        total = Solution.total
        totalMoney = 0
        weeks = n // ONE_WEEK
        days = n % ONE_WEEK
        for weekNum in range(weeks):
            totalMoney += weekly(weekNum)
        totalMoney += total(weeks+1,days)
        return totalMoney
    

s = Solution()
print(s.totalMoney(11))
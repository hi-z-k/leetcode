class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        maxWealth = 0
        for customer in accounts:
            for money in customer:
                wealth += money
            maxWealth = max(maxWealth, wealth)
            wealth = 0
        return maxWealth
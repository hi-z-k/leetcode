class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValid(capacity):
            nonlocal days
            day = 1
            curr_capacity = capacity
            for weight in weights:
                if curr_capacity - weight < 0:
                    day += 1
                    curr_capacity = capacity
                curr_capacity -= weight
            return day <= days

        low = max(weights)
        high = sum(weights)
        min_days = high
        while low <= high:
            middle = (low+high)//2
            if isValid(middle):
                min_days = min(min_days, middle)
                high = middle - 1
            else:
                low = middle + 1
        return min_days
            
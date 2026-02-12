class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = sum([i for i in nums if (i%2 == 0)])
        result_array = []
        for val, index in queries:
            inital = nums[index]
            if inital % 2 == 0:
                evenSum -= inital
            result = inital + val
            if result % 2 == 0:
                evenSum += result
            nums[index] = result
            result_array.append(evenSum)
        return result_array
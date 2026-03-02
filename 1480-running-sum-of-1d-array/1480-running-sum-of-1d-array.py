class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr_sum = 0
        sum_list = []
        for num in nums:
            curr_sum += num
            sum_list.append(curr_sum)
        return sum_list
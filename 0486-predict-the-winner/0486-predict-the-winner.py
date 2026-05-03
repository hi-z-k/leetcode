class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def play(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            return max(nums[0] - play(nums[1:]), nums[-1] - play(nums[:-1]))
        return play(nums) >= 0
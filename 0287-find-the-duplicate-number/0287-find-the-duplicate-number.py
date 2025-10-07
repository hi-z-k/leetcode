class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        turtle = 0
        rabbit = 0 
        while(True):
            turtle = nums[turtle]
            rabbit = nums[nums[rabbit]]
            if turtle == rabbit:
                break
        turtle = 0
        while(turtle != rabbit):
            turtle = nums[turtle]
            rabbit = nums[rabbit]
        return turtle
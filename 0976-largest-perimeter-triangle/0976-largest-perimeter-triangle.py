class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            sides = nums[i:i+3]
            c,a,b = sides
            if a + b > c:
                return sum(sides)
        return 0
        
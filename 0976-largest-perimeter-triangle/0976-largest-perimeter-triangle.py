class Solution:
    @staticmethod
    def check(triangle):
        if len(triangle) < 3:
            return False
        c,b,a = triangle
        return a + b > c
    def largestPerimeter(self, nums: List[int]) -> int:
        check = Solution.check
        nums.sort(reverse=True)
        n = 0
        best_case = nums[n:n+3]
        while n <= len(nums)-3:
            best_case = nums[n:n+3]
            if check(best_case):
                return sum(best_case)
            n += 1
        return 0

        
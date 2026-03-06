class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            width = right-left
            left_height = height[left]
            right_height = height[right]
            curr_height = min(left_height,right_height)
            max_area = max(max_area, curr_height*(width))
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        return max_area
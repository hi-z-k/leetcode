class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:    
        intersectList = []
        for num in set(nums1):
            if num in set(nums2):
                intersectList.append(num)
        return intersectList
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:    
        setNum2 = set()
        intersectSet = set()
        for num in nums2:
            setNum2.add(num)
        for num in nums1:
            if num in setNum2:
                intersectSet.add(num)
        return list(intersectSet)
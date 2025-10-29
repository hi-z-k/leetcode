class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idxHash = {}
        for i,num in enumerate(nums1):
            idxHash[num] = i
        stack = []
        result = [-1]*len(nums1)
        nums2.reverse()
        for num in nums2:
            while stack and stack[-1] <= num:
                stack.pop()
            if stack and num in idxHash:
                i = idxHash[num]
                result[i] = stack[-1]
            stack.append(num)
        return result
        
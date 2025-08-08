class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1Dict = Counter(nums1)
        num2Dict = Counter(nums2)

        commonList = []
        for num in num1Dict:
            if num in num2Dict:
                common = min(num1Dict[num], num2Dict[num])
                for i in range(common):
                    commonList.append(num)

        return commonList
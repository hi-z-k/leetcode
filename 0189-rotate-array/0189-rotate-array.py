class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        frontSection = []
        lastIdx = len(nums)-1
        lastK = -1*k
        # rescue the last k elements
        for i in range(lastK,0):
            frontSection.append(nums[i])
        # migrate the elements
        for i in range(lastIdx, -1, -1):
            nums[i] = nums[i-k]
            if i < k:
                nums[i] = frontSection[i] 

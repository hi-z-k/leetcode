class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
            
        nums.sort()
        i = 0

        max_length = len(nums)//3
        majority = []
        
        nums.append(float('inf'))
        
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                length = j - i
                if length > max_length:
                    majority.append(nums[i])
                i = j
                
        return majority
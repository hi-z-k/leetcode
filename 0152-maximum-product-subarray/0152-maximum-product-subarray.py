class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentProduct = 1
        minProduct = 1
        product = nums[0]
        for num in nums:
            tmp = currentProduct
            currentProduct = max(currentProduct*num,minProduct*num,num)
            minProduct = min(minProduct*num,tmp*num,num)
            product = max(currentProduct, product)
        return product

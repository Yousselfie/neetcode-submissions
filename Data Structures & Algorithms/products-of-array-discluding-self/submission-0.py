class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix
        pre = 1
        products = []
        for i in range(0,len(nums)):
            products.append(pre)
            pre *= nums[i]
        
        #postfix
        post = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] *= post
            post *= nums[i]
        
        return products

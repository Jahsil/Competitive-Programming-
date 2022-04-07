class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        product = 1 
        result = 0 
        maxProduct = float('-inf')
        
        
        start = 0 
        
        for end in range(len(nums)-1):
            product *= nums[end]
            
            if product == 0: 
                start += 1
                product = nums[end + 1]
                continue 
           
            if product >= maxProduct and product > 0:
                maxProduct = product 
            else:
                product /= nums[start]
                start += 1 
                
        return maxProduct
                
            
        

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first , second = float('inf') , float('inf')
        
        for i in nums:
            if i > second:
                return True 
            if i > first:
                second = min(second , i)
            first = min(first , i)
            
        return False

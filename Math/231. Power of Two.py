class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1 :
            return False
        while (n % 2 == 0):
            n/= 2
            
        return n == 1
    
    
# recursive solution

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True 
        if n < 1 :
            return False
        return self.isPowerOfTwo(n/2)
        

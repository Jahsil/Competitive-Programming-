# Using linear search (1648 ms)

class Solution:
    def mySqrt(self, x: int) -> int:
        y = 0 
        while (y*y <= x):
            y += 1
        return y - 1
      
# Using Binary Search 

class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0 
        end = x 
        
        while(start <= end):
            mid = start + (end -start)//2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                end = mid -1
            else:
                start = mid + 1
        return start -1

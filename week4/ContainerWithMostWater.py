class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxSize = 0
        start = 0 
        end = len(height) - 1
        while(start < end):
            if(height[start] <= height[end]):
                maxSize = max(maxSize , height[start] * (end-start))
                start += 1
            else:
                maxSize = max(maxSize , height[end] * (end-start))
                end -= 1
                
        return maxSize
        

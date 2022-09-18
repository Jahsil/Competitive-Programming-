class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        
        left = [0] * N
        right = [0] * N
        
        left[0] = height[0]
        for i in range(N):
            left[i] = max(left[i-1] , height[i])
            
        right[N-1] = height[N-1]
        for i in range(N-2 , -1 , -1):
            right[i] = max(right[i+1] , height[i])
        
        result = 0
        for i in range(N):
            target = min(left[i] , right[i])
            result += max(target - height[i] , 0)
            
        return result
            
            

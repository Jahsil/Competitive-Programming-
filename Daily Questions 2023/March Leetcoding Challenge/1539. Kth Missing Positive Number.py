class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = 0 
        counter = 0 

        for i in range(1 , (arr[-1] + k) + 1):
            if i in arr:
                continue 
            else:
                counter += 1
                ans = i
            
            if counter == k:
                return ans 

        return ans
        
            

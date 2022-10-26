class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = dict()
        d[0] = -1
        sm = 0
        for i , num in enumerate(nums):
            
            sm += num
            rem = sm % k
            print(sm , rem , d)
            if rem not in d:
                d[rem] = i
            elif i - d[rem] > 1 :
                return True
            
            
            
        return False
                

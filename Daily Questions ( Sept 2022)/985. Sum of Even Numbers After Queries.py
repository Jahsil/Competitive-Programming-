class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evens = sum(i for i in nums if i % 2 ==0)
        result = []
        
        for x , y in queries:
            prev = nums[y]
            nums[y] += x
            
            if prev % 2 == 0:
                if nums[y] % 2 == 0:
                    evens += x
                else:
                    evens -= prev
                    
            else:
                if nums[y] % 2 == 0:
                    evens += nums[y]
                    
            result.append(evens)
        
        return result

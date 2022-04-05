class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sCount , pCount = {} , {}
        result = []
        
        if len(p) > len(s):
            return []
        
        for i in range(len(p)):
            sCount[s[i]] = 1 + sCount.get(s[i] , 0) 
            pCount[p[i]] = 1 + pCount.get(p[i] , 0)
        if sCount == pCount:
            result.append(0)
        else:
            result = []
            
        start = 0
        plength = len(p)
        
        
        for end in range(len(p) , len(s)):
            sCount[s[end]] = 1 + sCount.get(s[end] , 0)
            sCount[s[start]] -= 1
            
            
            if sCount[s[start]] == 0:
                sCount.pop(s[start])
            start += 1 
            if sCount == pCount:
                result.append(start)
                
            
                
        return result
            
        
        
        
        
        
        

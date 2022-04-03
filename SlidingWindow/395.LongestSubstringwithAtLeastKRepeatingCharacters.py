class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0 or n < k :
            return 0 
        if k <= 1 :
            return n
        
        counts = Counter(s)
        
        i = 0 
        while i < n and counts[s[i]] >= k :
            i += 1
        
        if i >= n : return i
        
        firstPart = self.longestSubstring(s[0:i] , k)
        
        while i < n and counts[s[i]] < k:
            i += 1 
        if i < n:
            secondPart = self.longestSubstring(s[i:] , k)
        else:
            secondPart = 0
        return max(firstPart , secondPart)
      
      

      
      
        

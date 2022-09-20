class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        best = 0
        count = 0
        for c in range(len(s) - 1):
            if ord(s[c +1]) - ord(s[c]) == 1:
                count += 1
                best = max(best , count)
                
            else:
                count = 0
                
        return best + 1
        

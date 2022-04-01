# Using a set 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 
        result = 0 
        characters = set()
        
        for end in range(len(s)):
            while s[end] in characters:
                characters.remove(s[start])
                start += 1
            characters.add(s[end])
            result = max(result , end - start + 1)
        return result
        

  

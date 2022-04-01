# using set 

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
      
      
  # using hashmap
  
  class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = dict()
        start = 0 
        result = 0 
        
        for end in range(len(s)):
            if s[end] in characters.keys() and characters[s[end]] >= start:
                start = characters[s[end]] + 1
                characters[s[end]] = end
            else:
                characters[s[end]] = end
                result = max(result  , end - start + 1)
                
        return result
        

  

        

  

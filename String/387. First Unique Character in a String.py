class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = 0        
        for i in range(len(s)):
            if s[i] in freq.keys():
                freq[s[i]] += 1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
            
        return -1
    
    #using Counter -- much faster
    
    class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        print(freq)
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
            
        return -1
           

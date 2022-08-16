class Solution:
    def repeatedCharacter(self, s: str) -> str:
        se = set()
        for i in range(len(s)):
            if s[i] in se:
                return s[i]
            se.add(s[i])
            
            

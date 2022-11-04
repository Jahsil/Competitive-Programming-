class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1
        vowels = ['a' , 'e' , 'i' ,'o' , 'u','A' , 'E' , 'I' ,'O' , 'U']
        s = list(s)
        
        while start < end:
            if s[start] in vowels and s[end] not in vowels:
                end -= 1
            elif s[start] not in vowels and s[end]  in vowels:
                start += 1
                
            elif s[start] in vowels and s[end] in vowels:
                s[start] , s[end] = s[end] , s[start]
                start += 1
                end -= 1
            else :
                start += 1
                end -= 1
                
        return "".join(s)

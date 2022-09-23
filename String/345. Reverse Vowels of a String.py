class Solution:
    def reverseVowels(self, s: str) -> str:
        left , right = 0 , len(s) -1
        s = list(s)
        vowels = ['a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U']
        
        while left < right:
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1
            elif s[left] in vowels and s[right] in vowels :
                tmp = s[left]
                s[left] = s[right]
                s[right] = tmp
                
                left += 1
                right -= 1
            
                
        return "".join(s)
        

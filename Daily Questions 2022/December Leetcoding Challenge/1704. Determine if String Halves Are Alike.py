class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        first , second = 0 , 0
        
        for i , l in enumerate(s[:len(s) // 2]):
            if l in vowels:
                first += 1
        for i , l in enumerate(s[len(s) // 2:]):
            if l in vowels:
                second += 1
        return first == second
        

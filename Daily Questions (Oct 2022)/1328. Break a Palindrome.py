class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        pal = list(palindrome)
        N = len(pal)
        if len(palindrome) == 1:
            return ""
        start = 0
        for i in range(N):
            c = pal[i]
            if pal[i] != 'a':
                pal[i] = 'a'
                if "".join(pal) != "".join(pal)[::-1]:
                    return "".join(pal)
                else:
                    pal[i] = c
            start += 1
            if start == N:
                pal[start -1] = 'b'
            
        
        return "".join(pal)
        

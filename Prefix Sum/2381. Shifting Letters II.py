# TLE Not accepted

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        string = list(s)
        alpha = list(map(chr , range(97 , 123)))
        
        for start , end , direction in shifts:
            j = start
            for i in range(j , end + 1 ):
                if direction == 1:
                    string[i] = alpha[((alpha.index(string[i]) + 1) % len(alpha))]
                else:
                    string[i] = alpha[((alpha.index(string[i]) - 1) % len(alpha))]
                    
        return "".join(string)
    
    
    
    
    
# Using Prefix Sum (Accepted)
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N = len(s)
        shift = [0] * (N + 1)
        
        for start , end , direction in shifts:
            if direction == 1:
                shift[start] += 1
                shift[end + 1] -= 1
            else:
                shift[start] -= 1
                shift[end + 1] += 1
                
        
        for i in range(1,N):
            shift[i] += shift[i-1]
        
        result = []
        for i , c in enumerate(s):
            char = (ord(c) - ord('a') + shift[i]) % 26
            result.append(chr(char + ord('a')))
            
        return "".join(result)


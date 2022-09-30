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

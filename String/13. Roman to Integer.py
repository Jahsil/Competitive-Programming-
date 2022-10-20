class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
             "I": 1,
             "V": 5,     "IV": 4,
             "X": 10,    "IX": 9,
             "L": 50,    "XL": 40,
             "C": 100,   "XC": 90,
             "D": 500,   "CD": 400,
             "M": 1000,  "CM": 900,
        }
        result = 0
        N = len(s)
        i = 0
        while i < N:
            if s[i] == "I":
                if i + 1 < N  and s[i + 1] == "V":
                    result += roman["IV"]
                    i += 2
                    
                elif i + 1 < N  and s[i + 1] == "X":
                    result += roman["IX"]
                    i += 2
                else:
                    result += roman[s[i]]
                    i += 1
                    
            elif s[i] == "X":
                if i + 1 < N  and s[i + 1] == "L":
                    result += roman["XL"]
                    i += 2
                elif i + 1 < N  and s[i + 1] == "C":
                    result += roman["XC"]
                    i += 2
                else:
                    result += roman[s[i]]
                    i += 1
            elif s[i] == "C":
                if i + 1 < N  and s[i + 1] == "D":
                    result += roman["CD"]
                    i += 2
                elif i + 1 < N  and s[i + 1] == "M":
                    result += roman["CM"]
                    i += 2
                else:
                    result += roman[s[i]]
                    i += 1
            else:
                result += roman[s[i]]
                i += 1
        return result
            
            
       

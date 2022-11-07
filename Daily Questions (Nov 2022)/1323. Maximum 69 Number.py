class Solution:
    def maximum69Number (self, num: int) -> int:
        n = list(str(num))
        
        for i in range(len(n)):
            if n[i] == "9":
                continue
            else:
                n[i] = "9"
                break
                
        return "".join(n)

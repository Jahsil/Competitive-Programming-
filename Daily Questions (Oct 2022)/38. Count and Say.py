class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1" 
        c = self.countAndSay(n-1)
        out = ""
        for x , y in groupby(c):
            out += str(len(list(y))) + str(x)
            
        return out

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        c = Counter([int(i) for i in str(n)])
        print(c)
        i , nn = 0 , 0
        while nn < 10 ** 9:
            nn = 2 ** i
            d = Counter([int(i) for i in str(nn)]) 
            if c == d:
                return True
            i += 1
            
        return False
            

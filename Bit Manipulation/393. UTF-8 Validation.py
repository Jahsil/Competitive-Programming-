class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        N = len(data)
        
        i = 0
        while i < N:
            if (data[i] & (1 << 7)) == 0:
                i += 1 
                continue
                
            b = 0 
            while (data[i] & (1 << (7 - b))) > 0 and b <= 5:
                b += 1
            
            if b == 1 or b > 4:
                return False
            for j in range(1 , b):
                if i + j >= N:
                    return False
                if(data[i + j] & ((1 << 7) | (1 << 6))) != (1 << 7):
                    return False
                
            i += b
            
        return True
            
            
            
        

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        traversed = set()
        result = set()
        
        for i in range(len(s) - 9):
            currentSeq = s[i : i + 10]
            if currentSeq in traversed:
                result.add(currentSeq)
            traversed.add(currentSeq)
            
        return result
    
 
                
        
        

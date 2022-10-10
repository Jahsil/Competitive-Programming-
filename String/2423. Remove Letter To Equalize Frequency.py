class Solution:
    def equalFrequency(self, word: str) -> bool:
        N = len(word)
        count = Counter(word)
        
        if len(word) == 2 and word[0] != word[1]:
            return True
        for i , c in enumerate(word):
            count[c] -= 1
            
            if len(list(set(list(count.values())))) == 1:
                return True
            if count[c] == 0:
                del count[c]
                if len(list(set(list(count.values())))) == 1:
                    return True
                else:
                    count[c] == 0
            count[c] += 1
            
        return False
            
       

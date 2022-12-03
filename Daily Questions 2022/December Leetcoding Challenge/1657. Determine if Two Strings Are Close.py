class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 = Counter(word1)
        w2 = Counter(word2)
        sm1 = [v for k ,v in w1.items()]
        sm2 = [v for k ,v in w2.items()]
        s1 , s2 = Counter(sm1) , Counter(sm2)
        if s1 == s2 and (set(word1) == set(word2)):
            return True
        return False
    
    
    
#Another faster solution

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 , w2 = Counter(word1) , Counter(word2)
        return Counter(w1.values()) == Counter(w2.values()) and set(w1) == set(w2)

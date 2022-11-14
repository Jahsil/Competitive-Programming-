class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1 = Counter(words1)
        w2 = Counter(words2)
        ans = 0
        
        for word in words1:
            if w1[word] == 1 and w2[word] == 1:
                ans += 1
                
        return ans

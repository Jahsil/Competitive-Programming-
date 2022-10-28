class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 1

        while i < len(words):
            if sorted(words[i]) == sorted(words[i -1]):
                words.remove(words[i])
                continue

            i += 1
        return words
    
# Constant space
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        def getCount(word):
            count = [0] * 26 
            for c in word:
                count[ord(c) - ord('a')] += 1
            return count
        
        
        i = 0
        while i < len(words) - 1:
            if getCount(words[i]) == getCount(words[i + 1]):
                words.remove(words[i + 1])
                continue
            i += 1
        return words

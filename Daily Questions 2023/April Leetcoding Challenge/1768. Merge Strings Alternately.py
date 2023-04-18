class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        for x , y in zip(word1 , word2):
            merged += x
            merged += y
        if len(word2) > len(word1):
            merged += word2[len(word1) :]
        else:
            merged += word1[len(word2) : ]
        return merged
            

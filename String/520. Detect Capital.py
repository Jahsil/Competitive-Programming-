class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if word.upper() == word:
            return True
        if word.lower() == word:
            return True
        if word[0].isupper() == True and word[1:].islower() == True:
            return True
        
        return False

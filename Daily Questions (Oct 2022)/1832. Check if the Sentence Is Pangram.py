class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        words = "thequickbrownfoxjumpsoverthelazydog"
        for i in words:
            if i not in sentence:
                return False
            
        return True

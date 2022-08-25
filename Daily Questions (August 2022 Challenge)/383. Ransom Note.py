class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mcount = Counter(magazine)
        
        for i in range(len(ransomNote)):
            if mcount[ransomNote[i]] is not 0:
                mcount[ransomNote[i]] -= 1
            elif mcount[ransomNote[i]] not in mcount:
                return False
        return True
                

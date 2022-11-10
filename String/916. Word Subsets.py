class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        tmp = Counter()
        arr = []
        for w in words2:
            tmp |= Counter(w)
            
        for w in words1:
            if not tmp - Counter(w):
                arr.append(w)
                
        return arr

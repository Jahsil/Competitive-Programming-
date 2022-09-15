class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1: return []
        changed.sort()
        count = Counter(changed)
        
        res =  []
        
        for num in changed:
            if count[num] == 0: 
                continue
            elif count[num * 2] >= 1:
                res.append(num)
                count[num] -= 1
                count[num * 2] -= 1
            else: 
                return []
        
        return res

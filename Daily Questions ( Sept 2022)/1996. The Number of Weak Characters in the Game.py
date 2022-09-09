class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        mx = float('-inf')
        properties.sort(key = lambda x: (-x[0] , x[1]))
        weak = 0
        print(properties)
        for attack , deffence in properties:
            if deffence < mx:
                weak += 1
            mx = max(deffence , mx)
            
        return weak

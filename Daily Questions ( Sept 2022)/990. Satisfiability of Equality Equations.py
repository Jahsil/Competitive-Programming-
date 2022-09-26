class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = [i for i in range(26)]
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x ,y):
            a = find(x)
            b = find(y)
            
            parents[a] = b
            
        for equation in equations:
            
            if equation[1] == "!":
                continue
            a = ord(equation[0]) - ord('a')
            b = ord(equation[3]) - ord('a')
            
            union(a , b)
            
        for equation in equations:
            if equation[1] != "!":
                continue
                
            a = ord(equation[0]) - ord('a')
            b = ord(equation[3]) - ord('a')
            
            if find(a) == find(b):
                return False
        
        return True

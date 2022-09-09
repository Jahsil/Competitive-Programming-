class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []
        def dfs(value):
            if len(value) == n:
                result.append(''.join(map(str , value)))
                return
            
            last = value[-1]
            if 0 <= last + k <= 9:
                dfs(value + [last + k])
            if 0 <= last - k <= 9:
                dfs(value + [last - k])
                
        for i in range(1 , 10):
            dfs([i])
        return set(result)

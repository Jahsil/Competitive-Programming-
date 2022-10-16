class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        
        @lru_cache(None)
        def minDiff(index , dleft):
            if dleft == 0:
                if index == len(jobDifficulty): return 0
                return inf
            if index == len(jobDifficulty):
                return inf
            
            
            cost = 0
            result = inf
            
            for i in range(index , N):
                cost = max(cost , jobDifficulty[i])
                result = min(result , minDiff(i + 1 , dleft - 1) + cost)
            
            return result
        
        result = minDiff(0 , d)
        if result == float('inf'):
            return -1
        return result

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        N = len(nums)

        has_cache = [False] * (1 << N )
        cache = [None] * (1 << N )
        
        def dfs(mask , index):

            if has_cache[mask]:
                return cache[mask]
                
            ans = 0
            for i in range(N):
                if (mask & 1 << i) == 0:
                    for j in range(i + 1 , N):
                        if (mask & 1 << j) == 0:
                            ans = max(ans , dfs(mask | (1 << i) | (1 << j) , index + 1) + index * gcd(nums[i] , nums[j]  ))

            has_cache[mask] = True
            cache[mask] = ans

            return ans

        return dfs(0 , 1)

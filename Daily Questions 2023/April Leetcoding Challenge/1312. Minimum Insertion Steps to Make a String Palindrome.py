class Solution:
    def minInsertions(self, s: str) -> int:
        N = len(s)
        INF = 10 ** 20
        ans = INF
        
        has_cache = [[False] * (N + 1) for _ in range(N + 1)]
        cache = [[None] * (N + 1) for _ in range(N + 1)]
        

        def dfs(left , right):
            if left >= right:
                return 0

            if has_cache[left][right]:
                return cache[left][right]

            ans = INF
            if s[left] == s[right]:
                ans = min(ans , dfs(left + 1 , right - 1))

            else:
                ans = min(ans , dfs(left + 1 , right) + 1)
                ans = min(ans , dfs(left , right -1) + 1)

            has_cache[left][right] = True
            cache[left][right] = ans
            return cache[left][right]

        return dfs(0 , N - 1)

            
        

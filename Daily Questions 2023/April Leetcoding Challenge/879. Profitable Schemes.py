class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        MOD = 10 ** 9 + 7
        
        has_cache = [[[False] * (n + 1) for _ in range(minProfit + 1)] for _ in range(len(group) + 1)]
        cache = [[[False] * (n + 1) for _ in range(minProfit + 1)] for _ in range(len(group) + 1)]
        print(len(has_cache), len(has_cache[0]) , len(has_cache[0][0]) )
        

        def dfs(index , profit_left , n):
            
            if n < 0:
                return 0

            if profit_left < 0 :
                profit_left = 0

            if index == len(group):
                if profit_left == 0:
                    return 1
                return 0
            
            if has_cache[index][profit_left][n]:
                return cache[index][profit_left][n]

            left = dfs(index + 1 , profit_left - profit[index] , n - group[index])
            right = dfs(index + 1 , profit_left , n)

            has_cache[index][profit_left][n] = True
            cache[index][profit_left][n] = (left + right) % MOD

            return cache[index][profit_left][n]

        return dfs(0 , minProfit , n) % MOD

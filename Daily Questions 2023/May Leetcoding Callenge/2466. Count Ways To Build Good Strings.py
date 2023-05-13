class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        has_cache = [False] * (high + 1)
        cache = [None] * (high + 1)

        def dfs(string):
            if string > high:
                return 0
            if has_cache[string]:
                return cache[string]

            ans = 0
            if string >= low and string <= high:
                ans += 1
            ans += dfs(string +  zero) + dfs(string +  one)
            
            has_cache[string] = True
            cache[string] = ans % MOD
            return ans % MOD

        return dfs(0)

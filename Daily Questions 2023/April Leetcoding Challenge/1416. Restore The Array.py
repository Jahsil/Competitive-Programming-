class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        N = len(s)

        has_cache = [False] * N
        cache = [None] * N

        def dfs(index):
            if index == N :
                return 1 
            if s[index] == "0":
                return 0
            if has_cache[index]:
                return cache[index]

            curr = 0 
            total = 0 
            i = index
            while i < N and curr <= k:
                curr *= 10
                curr += int(s[i])

                if curr <= k:
                    total += dfs(i + 1)
                    total %= MOD
                else:
                    break
                i += 1

            has_cache[index] = True
            cache[index] = total % MOD
            
            return cache[index]

        return dfs(0)

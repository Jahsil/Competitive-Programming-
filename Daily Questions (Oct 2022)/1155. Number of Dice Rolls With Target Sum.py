class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        dp = {}
        
        def dfs(nleft , tar):
            if nleft == 0:
                if tar == 0:
                    return 1
                else:
                    return 0
            if tar < 0:
                return 0
            if (nleft , tar) in dp:
                return dp[(nleft , tar)]
            ans = 0 
            for i in range(1 , k + 1):
                ans += dfs(nleft -1 , tar - i)
                ans %= MOD
                
            dp[(nleft , tar)] = ans
            return ans
        
        return dfs(n , target)

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N = len(scores)
        arr = []
        arr = [[x,y] for x , y in zip(scores , ages)]
        arr = sorted(arr , key = lambda x : (x[1] , x[0]))
        dp = [i[0] for i in arr]
        for i in range(1 ,len(arr)):
            for j in range(i):
                if arr[j][0] <= arr[i][0]:
                    dp[i] = max(dp[i] , dp[j] + arr[i][0])
    
        return max(dp)

class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)

        def dfs(num):
            if int(num) < 10 and int(num) >= 0:
                return num

            ans = 0
            for i in range(len(num)):
                ans += int(num[i])

            return dfs(str(ans))
    
        return int(dfs(num))

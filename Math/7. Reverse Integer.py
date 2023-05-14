class Solution:
    def reverse(self, x: int) -> int:
        ans = str(x)[::-1]
        if x >= 0:
            if int(ans) <= 2 ** 31 -1 and int(ans) >= -2 ** 31:
                return int(ans)
            else:
                return 0
        elif x < 0:
            if int(ans[:len(ans)-1]) <= 2 ** 31 -1 and int(ans[:len(ans)-1]) >= -2 ** 31:
                return -1 * int(ans[:len(ans)-1])
            else:
                return 0
       

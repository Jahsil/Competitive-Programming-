class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            return "".join(sorted(s))
        ans = s
        N = len(s)
        for i in range(1 , N):
            curr = s[i:] + s[:i]
            ans = min(ans , curr)
        return ans

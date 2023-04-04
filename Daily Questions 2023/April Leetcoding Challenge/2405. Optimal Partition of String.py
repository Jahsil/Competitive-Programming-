class Solution:
    def partitionString(self, s: str) -> int:
        d = defaultdict(int)
        ans = 0 

        for i in range(len(s)):
            if s[i] in d:
                print("i ==" , i)
                ans += 1
                d = defaultdict(int)
                d[s[i]] += 1
            else:
                d[s[i]] += 1
        return ans + 1
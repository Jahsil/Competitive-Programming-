class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ans = 0
        c = Counter(tasks)
        for k , v in c.items():
            while v > 0 :
                if (v % 2 == 0 and v % 3 == 0) or (v % 3 == 0 ):
                    v -= 3
                    ans += 1
                else:
                    v -= 2 
                    ans += 1
                if v <= -1:
                    return -1
        return ans

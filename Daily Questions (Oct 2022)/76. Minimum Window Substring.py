class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount = Counter(t)
        scount = Counter()
        result = float('inf')
        left = -1
        start = 0
        N = len(s)
        arr = []
        
        for end in range(N):
            scount[s[end]] += 1
            
            while scount >= tcount:
                if result > end - start + 1:
                    result = end - start + 1
                    left = start
                
                scount[s[start]] -= 1
                start += 1
                
        if left == -1:
            return ""
        return s[left:left + result]

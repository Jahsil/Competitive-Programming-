class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        N = len(s)
        windowLength = len(words[0]) * (len(words))
        arr = []
        wcount = Counter(words)
        scount = Counter()
        start = 0
        left = -1
        for end in range(N):
            if end - start + 1 == windowLength:
                st = start
                en = start
                while en <= end:
                    if en - st + 1 == len(words[0]):
                        scount[s[st:en + 1]] += 1
                        st = en + 1
                    en += 1
                if scount == wcount:
                    left = start
                    arr.append(left)
                scount = Counter() 
                start += 1

        return arr
                
                
                    
             

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        N = len(s)
        vowels = "aeiou"
        tmp = []
        maxVowels , v = 0 , 0
        for end in range(N):
            tmp += s[end]
            if len(tmp) <= k:
                if s[end] in vowels:
                    v += 1  
            elif len(tmp) > k:
                if s[end] in vowels:
                    v += 1
                if tmp[0] in vowels:
                    v -= 1
                tmp.pop(0)
            maxVowels = max(maxVowels , v)
        return maxVowels

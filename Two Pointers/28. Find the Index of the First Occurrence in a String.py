class Solution:
    def strStr(self, haystack: str, needle: str) -> int:   
        end = len(haystack) - 1
        first = [i for i , h in enumerate(haystack) if needle[0] == h]
        for f in first:
            start = f 
            n = 0
            while start <= end :
                if needle[n] == haystack[start]:
                    if n == (len(needle) - 1):
                        return f
                    start += 1
                    n += 1
                else:
                    break

        return -1

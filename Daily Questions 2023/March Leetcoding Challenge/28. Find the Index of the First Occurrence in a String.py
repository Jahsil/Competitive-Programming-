class Solution:
    def strStr(self, haystack: str, needle: str) -> int:   
        N = len(haystack)
        for i in range(N):
            if haystack[i] == needle[0]:
                j = i
                k = 0
                start = j 
                while j < N and k < len(needle):
                    if haystack[j] == needle[k] and (j - start) == (len(needle) - 1):
                        return start
                    elif haystack[j] == needle[k]:
                        j += 1
                        k += 1
                        continue
                    else :
                        break

                    j += 1
                    k += 1

        return -1
                        
                    

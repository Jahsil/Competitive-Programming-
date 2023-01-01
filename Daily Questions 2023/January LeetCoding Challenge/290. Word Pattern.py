class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = defaultdict()
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i in range(len(s)):
            if i < len(pattern):
                if (pattern[i] not in d) and (s[i] not in d.values()):
                    d[pattern[i]] = s[i]

                else:
                    if pattern[i] in d:
                        if d[pattern[i]] !=  s[i]:
                            return False
                    else:
                        return False
            else:
                return False
            
        return True

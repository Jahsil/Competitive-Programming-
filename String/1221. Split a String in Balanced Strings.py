class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        # R = 1 , L = 0
        result = 0
        for i , c in enumerate(s):
            if c == 'R':
                count += 1
            else:
                count -= 1
            if count == 0:
                result += 1
                
        return result

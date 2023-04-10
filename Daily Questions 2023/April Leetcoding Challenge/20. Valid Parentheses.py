class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) <= 1 or len(s) % 2 != 0:
            return False
        for i in range(len(s)):     
            if (len(stack)) > 0 :
                if stack[-1] == "(" and s[i] == ")" or stack[-1] == "{" and s[i] == "}" or stack[-1] == "[" and s[i] == "]":
                    stack.pop()
                    continue
            stack.append(s[i])
            
        return True if len(stack) == 0 else False
            

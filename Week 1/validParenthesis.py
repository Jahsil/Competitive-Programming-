class Solution:
    def isValid(self, s: str) -> bool:
        balanced = True 
        length = len(s)
        arr = []
        counter = 0
        if not length%2 ==0:
            balanced = False 
            return balanced
        for i in range(0 , length):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                arr.append(s[i])
                counter += 1
            elif s[i] == ')' or s[i] =='}' or s[i] == ']':
                if arr :
                    a = arr.pop()
                    if a == '(' and s[i] == ')' and not length == 0 :
                        counter -= 1
                        continue
                    elif a == '{' and s[i] == '}' and not length == 0:
                        counter -= 1
                        continue
                    elif a == '[' and s[i] == ']' and not length == 0:
                        counter -= 1
                        continue
                    else :
                        balanced = False 
                        return balanced
                else:
                    balanced = False 
                    return balanced
        
        if counter == 0 :
            return True 
        else:
            return False
        

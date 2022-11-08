class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for i , l in enumerate(s):
            if len(stack) > 0 and abs(ord(stack[-1])-ord(l)) == 32 :
                stack.pop()
            else:        
                stack.append(l)
        return "".join(stack)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ["+","-","*","/"]

        for i , t in enumerate(tokens):
            if len(stack) > 1 and t in op:
                if t == "/":
                    b = stack.pop()
                    a = stack.pop()
                    res = a + t + b
                    c = int(eval(res))
                    stack.append((str(c)))
                else:
                    b = stack.pop()
                    a = stack.pop()
                    res = a + t + b
                    c = eval(res)
                    stack.append((str(c)))
            elif t not in op:
                stack.append(t)

        ans = int(float(stack[0]))
        return ans
   

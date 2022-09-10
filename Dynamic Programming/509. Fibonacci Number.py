class Solution:
    def fib(self, n: int) -> int:
        d = {}
        def recursion(index):
            if index == 1:
                return 1
            if index == 0:
                return 0
            if index in d:
                return d[index]
            d[index] = recursion(index - 1) + recursion(index - 2)
            
            return d[index]
        
        return recursion(n)

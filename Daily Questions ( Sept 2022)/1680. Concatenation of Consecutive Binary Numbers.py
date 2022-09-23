class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        arr = []
        def recursion(n):
            arr.append(bin(n))
            if n == 1:
                return 1
            recursion(n-1)
        recursion(n)
        newString = ""
        for i in range(len(arr)-1 , -1 , -1):
            newString += arr[i][2:]
        return int(newString , 2) % MOD
            

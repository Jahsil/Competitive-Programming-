class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        arr = []

        def dfs(index , tmp):
            if len(tmp) == k:
                return tmp
            elif len(tmp) > k:
                return []

            for i in range(index , n+1):
                arr.append(dfs(i+1 , tmp + [i]))
            

        dfs(1 , [])
        a = [i for i in arr if i != None]
        return a

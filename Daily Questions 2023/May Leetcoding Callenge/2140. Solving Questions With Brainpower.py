class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)

        has_cache = [False] * N
        cache = [None] * N


        def dfs(index):
            if index >= N :
                return 0

            if has_cache[index]:
                return cache[index]

            best = 0 
            a = dfs(index + questions[index][1] + 1) + questions[index][0]
            b = dfs(index + 1 )
 
            has_cache[index] = True
            cache[index] = max(a , b)

            return cache[index]

        return dfs(0)
            

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        N = len(strs)

        def calc_change(x , y):
            res = 0 
            for i , j in zip(x , y):
                if i != j :
                    res += 1
            return res

        adj_list = defaultdict(list)
        for i in range(N):
            for j in range(i + 1 , N):
                if calc_change(strs[i] , strs[j]) <= 2:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
      
       
        visited = [False] * N
        count = 0 

        def dfs(x):
            for v in adj_list[x]:
                if not visited[v]:
                    visited[v] = True
                    dfs(v)

        for i in range(N):
            if not visited[i]:
                count += 1
                visited[i] = True
                dfs(i)

        return count

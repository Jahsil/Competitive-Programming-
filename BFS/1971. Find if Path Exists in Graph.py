class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for u , v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        print(adj_list)
        
        q = deque()
        seen = [False] * n

        
        seen[source] = True
        q.append(source)
        
        while len(q) > 0 :
            popedItem = q.popleft()
            
            for i in adj_list[popedItem]:
                if not seen[i]:
                    seen[i] = True
                    q.append(i)

        return seen[destination]





        

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        d = {}
        d[start] = 0
        def change(x , y):
            count = 0
            for i , j in zip(x , y):
                if i != j:
                    count += 1
            return count
        
        q = deque()
        q.append(start)
        
        while q:
            curr = q.popleft()
            
            for b in bank:
                if b not in d and change(curr , b) <= 1:
                    d[b] = d[curr] + 1
                    q.append(b)
        if end not in d:
            return -1
        
        return d[end]

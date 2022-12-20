class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        adj_list = defaultdict(list)
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                adj_list[i].append(rooms[i][j])
        

        q = collections.deque()
        seen = [False] * N

        for i in range(N):
            if len(rooms[i]) == 0:
                seen[i] = True
        q.append(0)
        seen[0] = True

        while len(q) > 0 :
            popedItem = q.popleft()

            for val in adj_list[popedItem]:
                if not seen[val]:
                    seen[val] = True
                    q.append(val)

        return all(seen[i] == True for i in range(N))





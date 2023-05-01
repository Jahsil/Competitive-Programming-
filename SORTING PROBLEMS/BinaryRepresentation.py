import heapq

tasks = [[1,2],[2,4],[3,2],[4,1]]
heap = []
tasks = sorted(tasks , key = lambda x : (x[0] , x[1]))
print(tasks)

prev = tasks[0]
ans = []

while len(heap)>0:
    

print(heap)
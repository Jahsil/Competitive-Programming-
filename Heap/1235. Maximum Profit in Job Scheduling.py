class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = []
        res = 0
        Start = 1
        End = 0
        
        for s , e , p in zip(startTime , endTime , profit):
            arr.append((s , Start , e , p))
        heapq.heapify(arr)
        
        while len(arr) > 0:
            
            _ , t , px , qx = heapq.heappop(arr)
            
            if t == Start:
                e , p = px , qx
                heapq.heappush(arr , (e , End , res + p , -1))
                
            else:
                new_res = px
                res = max(res , new_res)
                
                
        return res
            
            
            

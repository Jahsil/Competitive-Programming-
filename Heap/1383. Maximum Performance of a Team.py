class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        
        heap = []
        performance = sorted(zip(speed , efficiency) , key = lambda x : -x[1]) 
        result = float('-inf')
        totalSpeed = 0 
        
        for s , e in performance:
            totalSpeed += s
            heapq.heappush(heap , s)
            
            if len(heap) > k:
                totalSpeed -= heapq.heappop(heap)
            result =  max(result , totalSpeed * e)
        return result % mod
            
            

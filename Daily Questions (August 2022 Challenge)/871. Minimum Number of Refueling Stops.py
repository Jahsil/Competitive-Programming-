class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        prev = 0
        output = 0
        fuel = startFuel
        
        for dist , gas in stations + [[target , 0]]:
            fuel -= (dist - prev)
            while heap and fuel < 0:
                fuel += -heappop(heap)
                output += 1
            if fuel < 0 :
                return -1
            heappush(heap , -gas)
            prev = dist
                
        return output

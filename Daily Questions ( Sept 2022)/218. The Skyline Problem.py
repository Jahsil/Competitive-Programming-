from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        
        for left , right , height in buildings:
            d[left].append((-1 , height))
            d[right].append((1 , height))

        sl = SortedList()
        sl.add(0)
        
        result = []
        last_height = 0
        
        for x in sorted(d.keys()):
            for t , h in d[x]:
                if t == -1:
                    sl.add(h)
                else:
                    sl.remove(h)
                    
            current_height = sl[-1]
            if current_height != last_height:
                result.append((x , current_height))
            last_height = current_height
                
                
        return result

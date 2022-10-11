class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x  : (x[0] , x[1]))
        result = 1
        prev_s , prev_e = points[0]
        
        for s , e in points:
            if s > prev_e:
                result += 1 
                prev_s , prev_e = s , e
            else:
                prev_e = min(prev_e , e)
                
        return result

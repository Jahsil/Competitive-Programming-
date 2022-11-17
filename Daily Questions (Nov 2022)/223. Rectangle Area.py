class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        
        nx1 = max(ax1 , bx1)
        ny1 = max(ay1 , by1)
        
        nx2 = min(ax2 , bx2)
        ny2 = min(ay2 , by2)
        intersection = 0
        if (nx2 - nx1) > 0 and (ny2 - ny1) > 0:
            intersection = (nx2 - nx1) * (ny2 - ny1)
        
        return area1 + area2 - intersection

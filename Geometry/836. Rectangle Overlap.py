class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        nx1 = max(rec1[0] , rec2[0])
        ny1 = max(rec1[1] , rec2[1])
        
        nx2 = min(rec1[2] , rec2[2])
        ny2 = min(rec1[3] , rec2[3])
        
        x_overlap = nx2 - nx1
        y_overlap = ny2 - ny1
        
        if x_overlap > 0 and y_overlap > 0:
            return True
        
        return False

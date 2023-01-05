class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points , key = lambda x : (x[0] , -x[1]))
        prev = points[0]
        ans = 1

        for i in range(1,len(points)):
            if points[i][0] <= prev[1] :
                prev[0] = points[i][0]
                prev[1] = min(prev[1] , points[i][1])
            else:
                ans += 1
                prev = points[i]
        return ans


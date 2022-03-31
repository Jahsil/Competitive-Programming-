class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        result = []
        currentInt = intervals[0]
        
        for i in range(1 , len(intervals)):
            if intervals[i][0] >= currentInt[0] and intervals[i][0] <= currentInt[1]:
                currentInt[1] = max(currentInt[1] , intervals[i][1])
            else:
                result.append(currentInt)
                currentInt = intervals[i]
        result.append(currentInt)
        return result

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            intervals.append(newInterval)
        print(intervals)
        for i in range(len(intervals)):
          
            if len(intervals) == 1:
                intervals.append(newInterval)
                break
            elif intervals[i][0] < newInterval[0]:
                continue
            else:
                intervals.insert(i , newInterval)
        if newInterval not in intervals:
            intervals.append(newInterval)
        print(intervals)
        
        intervals.sort()
       
        currentInt = intervals[0]
        result = []
        for i in range(1 , len(intervals)):
            if intervals[i][0] >= currentInt[0] and intervals[i][0] <= currentInt[1]:
                currentInt[1] = max(currentInt[1] , intervals[i][1])
            else:
                result.append(currentInt)
                currentInt = intervals[i]
        result.append(currentInt)
        return result
      
      
      # with O(1) space complexity 
      

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals.sort(key = lambda x : x[1])
        
        prevs , preve = intervals[0]
        result = 1
        for s , e in intervals:
            if s < preve:
                pass
            else:
                prevs , preve = s , e
                result += 1    
        return N - result

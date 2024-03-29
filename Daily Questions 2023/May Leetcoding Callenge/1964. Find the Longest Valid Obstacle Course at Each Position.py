class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lst,ans=[],[]
        for i in obstacles:
            b=bisect_right(lst,i)
            
            if b==len(lst):
                lst.append(i)
            else:
                lst[b]=i
            ans.append(b+1)
            
        return ans

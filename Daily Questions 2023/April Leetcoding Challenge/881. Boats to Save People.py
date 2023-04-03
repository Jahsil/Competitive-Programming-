class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        N = len(people)
        people.sort()
        start , end = 0 , N - 1
        ans = 0 

        while start <= end : 
            if people[start] + people[end] <= limit:
                start += 1 
                end -= 1
            else:
                end -= 1
                
            ans += 1
 
        return ans
                

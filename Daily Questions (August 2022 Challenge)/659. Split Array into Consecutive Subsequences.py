
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = Counter(nums)
        end = defaultdict(int)
        
        
        for num in nums:
            if count[num]:
                count[num] -= 1 
                
                if end[num - 1]:
                    end[num] += 1
                    end[num -1] -= 1
                elif count[num + 1] and count[num +2]:
                    count[num + 1] -= 1
                    count[num + 2] -= 1
                    end[num +2] += 1
                else:
                    return False
                
        return True
      

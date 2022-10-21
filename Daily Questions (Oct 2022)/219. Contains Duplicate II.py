class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = collections.defaultdict(list)
        N = len(nums)
        
        for i in range(N):
            d[nums[i]].append(i)
            
        for x , y in d.items():
            if len(y) > 1:
                diff = float('inf')
                for i in range(len(y) - 1):
                    if y[i + 1] - y[i] < diff:
                        diff = abs(y[i + 1] - y[i])
                if diff <= k:
                    return True
                
        return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        traversed = dict()
        start = 0 
        for end in range(len(nums)):
            if nums[end] in traversed.keys():
                if abs(traversed[nums[end]] - end) <= k:
                    return True
            traversed[nums[end]] = end
        return False
       

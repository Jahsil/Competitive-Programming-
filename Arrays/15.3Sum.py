class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        length = len(nums) -2
        for i in range(0,length):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                start = i+1
                end = len(nums) -1
                summ = 0 - nums[i]

                while(start < end):
                    if nums[start] + nums[end] == summ:
                        arr.append([nums[i] , nums[start] , nums[end]])
                        while(start < end and nums[start] == nums[start+1]):
                            start += 1
                        while(start < end and nums[end] == nums[end-1]):
                            end -= 1
                        start += 1
                        end -= 1
                    elif nums[start] + nums[end] > summ:
                        end -= 1
                    else:
                        start += 1
        return arr
                        
                    
                    
                
            

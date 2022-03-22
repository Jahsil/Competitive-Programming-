class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        arr = []
        unique = set()
        for i in range(len(nums) -3):
            threeSumm = target - nums[i]
            for j in range(i+1 , len(nums) -2):
                start = j + 1 
                end = len(nums) -1
                summ = threeSumm - nums[j]
                while(start < end):
                    if nums[start] + nums[end] == summ:
                        if (nums[i] , nums[j] , nums[start] , nums[end]) not in unique:
                            unique.add((nums[i] , nums[j] , nums[start] , nums[end]))
                            arr.append([nums[i] , nums[j] , nums[start] , nums[end]])
                        start += 1
                        end -= 1

                    elif nums[start] + nums[end] < summ:
                        start += 1
                    else:
                        end -= 1
        return arr


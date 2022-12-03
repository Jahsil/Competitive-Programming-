class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        nums = list(num)
        for i , n in enumerate(nums):
            if int(change[int(n)]) >= int(n):
                nums[i] = str(change[int(n)])
            elif list(nums) != list(num):
                break
            else:
                continue
        return "".join(nums)

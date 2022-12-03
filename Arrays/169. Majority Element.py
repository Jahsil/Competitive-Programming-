class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        return [k for k ,v in c.items() if v >= len(nums) / 2][0]

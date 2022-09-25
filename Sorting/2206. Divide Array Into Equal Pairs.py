class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for x , y in freq.items():
            if y % 2 != 0 or len(nums) % 2 != 0:
                return False
        return True

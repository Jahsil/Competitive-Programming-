class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        d = defaultdict(int)
        d[0] = 1
        sm = 0
        result = 0
        for i in range(N):
            sm += nums[i]
            if sm - k in d:
                result += d[sm - k]
            d[sm] += 1
            
        return result

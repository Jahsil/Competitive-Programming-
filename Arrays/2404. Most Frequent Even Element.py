class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            if num % 2 == 0:
                d[num] += 1
        c = sorted(d.items() , key = lambda x : (-x[1] , x[0]))
        return c[0][0] if len(c) > 0 else -1

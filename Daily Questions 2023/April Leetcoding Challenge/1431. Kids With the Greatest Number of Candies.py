class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        res = [False for _ in range(len(candies))]

        for i , candy in enumerate(candies):
            if candy + extraCandies >= maxCandy:
                res[i] = True
        return res

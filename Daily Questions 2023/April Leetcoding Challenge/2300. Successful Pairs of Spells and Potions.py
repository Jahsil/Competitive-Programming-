class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n , m = len(spells) , len(potions)
        tmp = [success / spells[i] for i in range(len(spells))]
        ans = [0] * len(spells) 
        potions.sort()
        for i in range(len(spells)):
            index = bisect.bisect_left(potions , tmp[i])
            if index < m and index >= 0:
                ans[i] = m - index
        return ans

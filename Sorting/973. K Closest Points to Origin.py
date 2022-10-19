class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origin = 0
        result = [( x , y ,  math.sqrt((x - origin) ** 2 + (y - origin) ** 2) )for x , y in points]
        ans = []
        i = 0
        for x , y , d in sorted(result , key = lambda x : x[2]):
            if i < k:
                ans.append([x , y])
                i += 1
            else:
                break

        return ans

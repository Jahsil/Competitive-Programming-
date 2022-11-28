class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = []
        for i , v in enumerate(score):
            arr.append((-1 * v , i ))
        heapq.heapify(arr)
        ans = []
        k = 3
        N = len(arr)
        while len(arr) > 0:
            val = heapq.heappop(arr)
            if N - len(arr) == 1:
                score[val[1]] = "Gold Medal"
            elif N - len(arr) == 2:
                score[val[1]] = "Silver Medal"
            elif N - len(arr) == 3:
                score[val[1]] = "Bronze Medal"
            else:
                k += 1
                score[val[1]] = str(k)
                
        return score

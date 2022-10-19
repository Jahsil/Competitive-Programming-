class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        count = sorted(count.items() , key= lambda x : (-x[1] , x[0]))
        result = []
        for i in range(k):
            result.append(count[i][0])
        return result

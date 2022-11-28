class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        matcheswon = defaultdict(int)
        matcheslost = defaultdict(int)
        for x , y in matches:
            matcheswon[x] += 1
            matcheslost[y] += 1
        nx = []
        for x , y in matcheswon.items():
            if x not in matcheslost:
                nx.append(x)
        ny = [x for x , y  in matcheslost.items() if y == 1 ]
        return [sorted(nx) , sorted(ny)]

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = sorted(Counter(s).items() , key = lambda x : -x[1])
        return "".join([k * v for k , v in freq])

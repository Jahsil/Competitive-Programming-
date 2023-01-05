class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCount , tCount= Counter(s) , Counter(t)
        return list(tCount - sCount)[0]

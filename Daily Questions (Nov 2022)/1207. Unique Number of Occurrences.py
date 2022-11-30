class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        s = set()
        for k , v in c.items():
            if v in s:
                return False
            s.add(v)
        return True
